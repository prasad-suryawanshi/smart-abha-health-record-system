#!/usr/bin/env python
"""
Database initialization script with sample data for Smart ABHA
"""

from app import create_app
from models import db, User, UserRole, MaternalRecord, ChildRecord, Checkup, Vaccination, GrowthMetric, Reminder
from datetime import datetime, timedelta

def init_database():
    """Initialize database with sample data"""
    
    # Create app
    app = create_app('development')
    
    with app.app_context():
        # Drop all tables (only in development!)
        print("🗑️  Dropping existing tables...")
        db.drop_all()
        
        # Create all tables
        print("📁 Creating database tables...")
        db.create_all()
        
        # Create demo users
        print("👥 Creating demo users...")
        users = [
            User(name='Rajesh Kumar', email='admin@smartabha.com', role=UserRole.ADMIN, active=True),
            User(name='Dr. Amit Sharma', email='doctor@smartabha.com', role=UserRole.DOCTOR, active=True),
            User(name='Priya Patil', email='asha@smartabha.com', role=UserRole.ASHA, active=True),
            User(name='Sunita Pawar', email='anganwadi@smartabha.com', role=UserRole.ANGANWADI, active=True),
            User(name='Neha Sharma', email='mother@smartabha.com', role=UserRole.MOTHER, active=True),
        ]
        passwords = {
            'admin@smartabha.com': 'Admin@123',
            'doctor@smartabha.com': 'Doctor@123',
            'asha@smartabha.com': 'Asha@123',
            'anganwadi@smartabha.com': 'Anganwadi@123',
            'mother@smartabha.com': 'Mother@123',
        }
        for user in users:
            user.set_password(passwords[user.email])
            db.session.add(user)
        db.session.commit()
        print("✅ Users created successfully")
        
        # Create maternal records
        print("👩‍🤰 Creating maternal records...")
        today = datetime.now().date()
        
        maternal_records = [
            MaternalRecord(
                abha_id='ABHA-2024-001',
                mother_name='Lakshmi Devi',
                age=28,
                phone='9876543210',
                address='Village: Bhimpur, District: Madhya Pradesh',
                pregnancy_status='Active',
                lmp_date=today - timedelta(days=180),
                edd=today + timedelta(days=90),
                weeks_of_pregnancy=20,
                blood_group='O',
                rhesus='Positive',
                medical_conditions='Anemia',
                allergies='None',
                created_by=users[0].id
            ),
            MaternalRecord(
                abha_id='ABHA-2024-002',
                mother_name='Priya Reddy',
                age=32,
                phone='9876543211',
                address='Village: Telangpur, District: Telangana',
                pregnancy_status='Completed',
                lmp_date=today - timedelta(days=300),
                edd=today - timedelta(days=100),
                weeks_of_pregnancy=40,
                blood_group='AB',
                rhesus='Negative',
                medical_conditions='None',
                allergies='Penicillin',
                created_by=users[0].id
            ),
        ]
        
        for record in maternal_records:
            db.session.add(record)
        
        db.session.commit()
        print("✅ Maternal records created successfully")
        
        # Create checkups for maternal records
        print("🏥 Creating maternal checkups...")
        for maternal in maternal_records:
            checkup = Checkup(
                maternal_record_id=maternal.id,
                checkup_type='Prenatal',
                checkup_date=today - timedelta(days=30),
                weight=58.5,
                blood_pressure='120/80',
                temperature=98.6,
                findings='Normal pregnancy progress',
                diagnosis='Healthy pregnancy',
                follow_up_date=today + timedelta(days=30)
            )
            db.session.add(checkup)
        
        db.session.commit()
        print("✅ Maternal checkups created successfully")
        
        # Create child records
        print("👶 Creating child records...")
        child_records = [
            ChildRecord(
                abha_id='ABHA-2024-CH-001',
                child_name='Arjun Devi',
                gender='Male',
                date_of_birth=today - timedelta(days=365),
                birth_weight=3.2,
                birth_length=50,
                birth_place='District Hospital, Madhya Pradesh',
                birth_type='Normal',
                mother_name='Lakshmi Devi',
                blood_group='O',
                allergies='None',
                created_by=users[0].id
            ),
            ChildRecord(
                abha_id='ABHA-2024-CH-002',
                child_name='Anjali Sharma',
                gender='Female',
                date_of_birth=today - timedelta(days=180),
                birth_weight=2.8,
                birth_length=48,
                birth_place='Community Health Center, Telangana',
                birth_type='Cesarean',
                mother_name='Priya Reddy',
                blood_group='AB',
                allergies='Eggs',
                created_by=users[0].id
            ),
        ]
        
        for record in child_records:
            db.session.add(record)
        
        db.session.commit()
        print("✅ Child records created successfully")
        
        # Create vaccinations
        print("💉 Creating vaccination records...")
        vaccines = [
            ('BCG', 'Completed'),
            ('OPV-1', 'Completed'),
            ('OPV-2', 'Completed'),
            ('DPT-1', 'Completed'),
            ('Hepatitis B', 'Pending'),
            ('Measles', 'Pending'),
        ]
        
        for child in child_records:
            for vaccine_name, status in vaccines:
                vaccination = Vaccination(
                    child_record_id=child.id,
                    vaccine_name=vaccine_name,
                    scheduled_date=today - timedelta(days=90) if status == 'Completed' else today + timedelta(days=30),
                    status=status,
                    notes=f'{vaccine_name} - {status}'
                )
                db.session.add(vaccination)
        
        db.session.commit()
        print("✅ Vaccinations created successfully")
        
        # Create growth metrics
        print("📈 Creating growth metrics...")
        for child in child_records:
            growth = GrowthMetric(
                child_record_id=child.id,
                measurement_date=today - timedelta(days=30),
                age_months=12 if 'Arjun' in child.child_name else 6,
                weight=10.5 if 'Arjun' in child.child_name else 8.2,
                height=75 if 'Arjun' in child.child_name else 65,
                head_circumference=45 if 'Arjun' in child.child_name else 42,
                weight_for_age='Normal',
                height_for_age='Normal'
            )
            db.session.add(growth)
        
        db.session.commit()
        print("✅ Growth metrics created successfully")
        
        # Create reminders
        print("🔔 Creating reminders...")
        reminders = [
            Reminder(
                title='Antenatal Checkup - Lakshmi Devi',
                description='Monthly antenatal checkup for 20 weeks pregnancy',
                reminder_type='Checkup',
                maternal_record_id=maternal_records[0].id,
                due_date=today + timedelta(days=5),
                priority='High'
            ),
            Reminder(
                title='DPT Vaccination - Arjun Devi',
                description='DPT vaccine administration',
                reminder_type='Vaccination',
                child_record_id=child_records[0].id,
                due_date=today + timedelta(days=10),
                priority='Critical'
            ),
            Reminder(
                title='Growth Monitoring - Anjali Sharma',
                description='Check weight and height progress',
                reminder_type='Checkup',
                child_record_id=child_records[1].id,
                due_date=today + timedelta(days=7),
                priority='Medium'
            ),
            Reminder(
                title='Postnatal Checkup - Priya Reddy',
                description='Post-delivery checkup and assessment',
                reminder_type='Checkup',
                maternal_record_id=maternal_records[1].id,
                due_date=today - timedelta(days=5),
                priority='High',
                completed=True,
                completed_date=today - timedelta(days=5)
            ),
        ]
        
        for reminder in reminders:
            db.session.add(reminder)
        
        db.session.commit()
        print("✅ Reminders created successfully")
        
        # Print summary
        print("\n" + "="*50)
        print("✨ DATABASE INITIALIZATION COMPLETE ✨")
        print("="*50)
        print("\n📊 Summary:")
        print(f"  👥 Users created: {len(users)}")
        print(f"  👩‍🤰 Maternal records: {len(maternal_records)}")
        print(f"  👶 Child records: {len(child_records)}")
        print(f"  💉 Vaccinations: {len(child_records) * len(vaccines)}")
        print(f"  📈 Growth metrics: {len(child_records)}")
        print(f"  🔔 Reminders: {len(reminders)}")
        
        print("\n👤 Demo Users:")
        for user in users:
            print(f"  • {user.name}")
            print(f"    Email: {user.email}")
            print(f"    Role: {user.role.value.upper()}")
            print(f"    Password: (see documentation)\n")
        
        print("\n🌐 Access the application:")
        print("  http://localhost:5000")
        print("\n" + "="*50)


if __name__ == '__main__':
    init_database()
