"""
Smart ABHA Healthcare Management System
Complete Flask Backend
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import config
from models import (
    db, User, UserRole, MaternalRecord, ChildRecord,
    Checkup, Vaccination, GrowthMetric, Reminder, Notification
)
from datetime import datetime, timedelta
import re

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'Please log in to continue.'
    login_manager.login_message_category = 'error'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    # ===================== PUBLIC =====================

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            email = (request.form.get('email') or '').strip().lower()
            password = request.form.get('password') or ''
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user, remember=True)
                flash(f'Welcome back, {user.name}!', 'success')
                return redirect(url_for('dashboard'))
            flash('Invalid email or password.', 'error')
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            name = (request.form.get('name') or '').strip()
            email = (request.form.get('email') or '').strip().lower()
            role_str = request.form.get('role') or 'asha'
            password = request.form.get('password') or ''
            confirm = request.form.get('confirm_password') or ''

            errors = []
            if not name or len(name) < 2:
                errors.append('Name must be at least 2 characters.')
            if not email or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                errors.append('Enter a valid email address.')
            if User.query.filter_by(email=email).first():
                errors.append('This email is already registered.')
            if len(password) < 6:
                errors.append('Password must be at least 6 characters.')
            if password != confirm:
                errors.append('Passwords do not match.')

            role_map = {
                'doctor': UserRole.DOCTOR,
                'asha': UserRole.ASHA,
                'anganwadi': UserRole.ANGANWADI,
                'admin': UserRole.ADMIN,
                'mother': UserRole.MOTHER,
            }
            role = role_map.get(role_str, UserRole.ASHA)

            if errors:
                for e in errors:
                    flash(e, 'error')
                return render_template('register.html', form=request.form)

            user = User(name=name, email=email, role=role, active=True)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully. Please log in.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route('/quick-login/<int:user_id>')
    def quick_login(user_id):
        user = User.query.get(user_id)
        if user:
            login_user(user)
            flash(f'Logged in as {user.name}', 'success')
            return redirect(url_for('dashboard'))
        flash('User not found.', 'error')
        return redirect(url_for('login'))

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'success')
        return redirect(url_for('index'))

    # ===================== DASHBOARD =====================

    @app.route('/dashboard')
    @login_required
    def dashboard():
        total_maternal = MaternalRecord.query.count()
        total_child = ChildRecord.query.count()
        total_reminders = Reminder.query.filter_by(completed=False).count()
        today = datetime.utcnow().date()
        overdue = Reminder.query.filter(
            Reminder.completed == False,
            Reminder.due_date < today
        ).count()
        reminders = Reminder.query.filter_by(completed=False).order_by(Reminder.due_date).limit(5).all()
        maternal_records = MaternalRecord.query.order_by(MaternalRecord.created_at.desc()).limit(4).all()
        child_records = ChildRecord.query.order_by(ChildRecord.created_at.desc()).limit(4).all()
        return render_template(
            'dashboard.html',
            total_maternal=total_maternal,
            total_child=total_child,
            total_reminders=total_reminders,
            overdue_reminders=overdue,
            reminders=reminders,
            maternal_records=maternal_records,
            child_records=child_records,
        )

    # ===================== MATERNAL =====================

    @app.route('/maternal')
    @login_required
    def maternal_list():
        records = MaternalRecord.query.order_by(MaternalRecord.created_at.desc()).all()
        return render_template('maternal_list.html', records=records)

    @app.route('/maternal/new', methods=['GET', 'POST'])
    @login_required
    def maternal_new():
        if request.method == 'POST':
            abha_id = (request.form.get('abha_id') or '').strip()
            mother_name = (request.form.get('mother_name') or '').strip()
            if not abha_id or not mother_name:
                flash('ABHA ID and Mother Name are required.', 'error')
                return render_template('maternal_form.html')
            if MaternalRecord.query.filter_by(abha_id=abha_id).first():
                flash('This ABHA ID already exists.', 'error')
                return render_template('maternal_form.html')
            record = MaternalRecord(
                abha_id=abha_id,
                mother_name=mother_name,
                age=request.form.get('age') or None,
                phone=request.form.get('phone'),
                address=request.form.get('address'),
                pregnancy_status=request.form.get('pregnancy_status') or 'Active',
                weeks_of_pregnancy=request.form.get('weeks_of_pregnancy') or None,
                blood_group=request.form.get('blood_group'),
                medical_conditions=request.form.get('medical_conditions'),
                created_by=current_user.id,
            )
            age = request.form.get('age')
            if age:
                record.age = int(age)
            weeks = request.form.get('weeks_of_pregnancy')
            if weeks:
                record.weeks_of_pregnancy = int(weeks)
            db.session.add(record)
            db.session.commit()
            flash('Maternal record created.', 'success')
            return redirect(url_for('maternal_detail', id=record.id))
        return render_template('maternal_form.html')

    @app.route('/maternal/<int:id>')
    @login_required
    def maternal_detail(id):
        record = MaternalRecord.query.get_or_404(id)
        checkups = Checkup.query.filter_by(maternal_record_id=id).order_by(Checkup.checkup_date.desc()).all()
        return render_template('maternal_detail.html', record=record, checkups=checkups)

    @app.route('/maternal/<int:id>/checkup', methods=['POST'])
    @login_required
    def maternal_add_checkup(id):
        record = MaternalRecord.query.get_or_404(id)
        checkup = Checkup(
            maternal_record_id=record.id,
            checkup_type=request.form.get('checkup_type') or 'Prenatal',
            checkup_date=datetime.strptime(request.form.get('checkup_date'), '%Y-%m-%d').date() if request.form.get('checkup_date') else datetime.utcnow().date(),
            weight=float(request.form['weight']) if request.form.get('weight') else None,
            blood_pressure=request.form.get('blood_pressure'),
            findings=request.form.get('findings'),
            notes=request.form.get('notes'),
        )
        db.session.add(checkup)
        db.session.commit()
        flash('Checkup added.', 'success')
        return redirect(url_for('maternal_detail', id=id))

    # ===================== CHILD =====================

    @app.route('/child')
    @login_required
    def child_list():
        records = ChildRecord.query.order_by(ChildRecord.created_at.desc()).all()
        return render_template('child_list.html', records=records)

    @app.route('/child/new', methods=['GET', 'POST'])
    @login_required
    def child_new():
        if request.method == 'POST':
            abha_id = (request.form.get('abha_id') or '').strip()
            child_name = (request.form.get('child_name') or '').strip()
            dob = request.form.get('date_of_birth')
            if not abha_id or not child_name or not dob:
                flash('ABHA ID, Child Name and Date of Birth are required.', 'error')
                return render_template('child_form.html')
            if ChildRecord.query.filter_by(abha_id=abha_id).first():
                flash('This ABHA ID already exists.', 'error')
                return render_template('child_form.html')
            record = ChildRecord(
                abha_id=abha_id,
                child_name=child_name,
                gender=request.form.get('gender'),
                date_of_birth=datetime.strptime(dob, '%Y-%m-%d').date(),
                created_by=current_user.id,
            )
            db.session.add(record)
            db.session.commit()
            flash('Child record created.', 'success')
            return redirect(url_for('child_detail', id=record.id))
        return render_template('child_form.html')

    @app.route('/child/<int:id>')
    @login_required
    def child_detail(id):
        record = ChildRecord.query.get_or_404(id)
        vaccinations = Vaccination.query.filter_by(child_record_id=id).order_by(Vaccination.vaccination_date.desc()).all()
        growth = GrowthMetric.query.filter_by(child_record_id=id).order_by(GrowthMetric.measurement_date.desc()).all()
        checkups = Checkup.query.filter_by(child_record_id=id).order_by(Checkup.checkup_date.desc()).all()
        return render_template(
            'child_detail.html',
            record=record,
            vaccinations=vaccinations,
            growth=growth,
            checkups=checkups,
        )

    @app.route('/child/<int:id>/vaccination', methods=['POST'])
    @login_required
    def child_add_vaccination(id):
        record = ChildRecord.query.get_or_404(id)
        v = Vaccination(
            child_record_id=record.id,
            vaccine_name=request.form.get('vaccine_name') or 'Vaccine',
            administered_date=datetime.strptime(request.form.get('administered_date'), '%Y-%m-%d').date() if request.form.get('administered_date') else datetime.utcnow().date(),
            lot_number=request.form.get('lot_number'),
            status=request.form.get('status') or 'Completed',
            notes=request.form.get('notes'),
        )
        db.session.add(v)
        db.session.commit()
        flash('Vaccination recorded.', 'success')
        return redirect(url_for('child_detail', id=id))

    @app.route('/child/<int:id>/growth', methods=['POST'])
    @login_required
    def child_add_growth(id):
        record = ChildRecord.query.get_or_404(id)
        g = GrowthMetric(
            child_record_id=record.id,
            measurement_date=datetime.strptime(request.form.get('measurement_date'), '%Y-%m-%d').date() if request.form.get('measurement_date') else datetime.utcnow().date(),
            weight=float(request.form['weight']) if request.form.get('weight') else None,
            height=float(request.form['height']) if request.form.get('height') else None,
            age_months=int(request.form['age_months']) if request.form.get('age_months') else None,
            weight_for_age=request.form.get('weight_for_age') or 'Normal',
            notes=request.form.get('notes'),
        )
        db.session.add(g)
        db.session.commit()
        flash('Growth record added.', 'success')
        return redirect(url_for('child_detail', id=id))

    # ===================== ANALYTICS =====================

    @app.route('/analytics')
    @login_required
    def analytics():
        stats = {
            'total_maternal': MaternalRecord.query.count(),
            'total_child': ChildRecord.query.count(),
            'total_checkups': Checkup.query.count(),
            'total_vaccinations': Vaccination.query.count(),
            'total_reminders': Reminder.query.filter_by(completed=False).count(),
        }
        at_risk = MaternalRecord.query.filter(MaternalRecord.age >= 35).count()
        growth_data = GrowthMetric.query.order_by(GrowthMetric.measurement_date.desc()).limit(20).all()
        return render_template('analytics.html', stats=stats, at_risk_maternal=at_risk, growth_data=growth_data)


    # ===================== LISTS: VACCINATION / CHECKUPS / GROWTH =====================

    @app.route('/vaccinations')
    @login_required
    def vaccination_list():
        records = Vaccination.query.order_by(Vaccination.created_at.desc()).all()
        return render_template('vaccination_list.html', records=records)

    @app.route('/checkups')
    @login_required
    def checkup_list():
        records = Checkup.query.order_by(Checkup.checkup_date.desc()).all()
        return render_template('checkup_list.html', records=records)

    @app.route('/growth')
    @login_required
    def growth_list():
        records = GrowthMetric.query.order_by(GrowthMetric.measurement_date.desc()).all()
        return render_template('growth_list.html', records=records)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            flash('Thank you! Your message has been received (demo only).', 'success')
            return redirect(url_for('contact'))
        return render_template('contact.html')

    # ===================== ERRORS =====================

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        db.session.rollback()
        return render_template('500.html'), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
