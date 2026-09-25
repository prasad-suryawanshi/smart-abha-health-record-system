from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import enum

db = SQLAlchemy()


class UserRole(enum.Enum):
    """User roles in the system"""
    DOCTOR = "doctor"
    ASHA = "asha"
    ANGANWADI = "anganwadi"
    ADMIN = "admin"
    MOTHER = "mother"


class User(UserMixin, db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.ASHA, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.email}>'


class MaternalRecord(db.Model):
    """Maternal health record"""
    __tablename__ = 'maternal_records'
    
    id = db.Column(db.Integer, primary_key=True)
    abha_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    mother_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    
    # Pregnancy details
    pregnancy_status = db.Column(db.String(50))  # Active, Completed, Miscarriage, etc.
    lmp_date = db.Column(db.Date)  # Last Menstrual Period
    edd = db.Column(db.Date)  # Estimated Delivery Date
    weeks_of_pregnancy = db.Column(db.Integer)
    
    # Medical history
    blood_group = db.Column(db.String(5))
    rhesus = db.Column(db.String(5))  # Positive/Negative
    medical_conditions = db.Column(db.Text)
    allergies = db.Column(db.Text)
    
    # Checkup history
    checkups = db.relationship('Checkup', backref='maternal_record', lazy=True, cascade='all, delete-orphan')
    
    # Created by and for tracking
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<MaternalRecord {self.abha_id}>'


class Checkup(db.Model):
    """Medical checkup record"""
    __tablename__ = 'checkups'
    
    id = db.Column(db.Integer, primary_key=True)
    maternal_record_id = db.Column(db.Integer, db.ForeignKey('maternal_records.id'), nullable=True)
    child_record_id = db.Column(db.Integer, db.ForeignKey('child_records.id'), nullable=True)
    
    checkup_type = db.Column(db.String(50))  # Prenatal, Postnatal, General, etc.
    checkup_date = db.Column(db.Date, nullable=False)
    
    # Vital signs
    weight = db.Column(db.Float)
    blood_pressure = db.Column(db.String(20))  # e.g., "120/80"
    temperature = db.Column(db.Float)
    height = db.Column(db.Float)
    
    # Assessment
    findings = db.Column(db.Text)
    diagnosis = db.Column(db.Text)
    treatment = db.Column(db.Text)
    
    # Follow-up
    follow_up_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Checkup {self.checkup_date}>'


class ChildRecord(db.Model):
    """Child health record"""
    __tablename__ = 'child_records'
    
    id = db.Column(db.Integer, primary_key=True)
    abha_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    child_name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(20))  # Male, Female, Other
    date_of_birth = db.Column(db.Date, nullable=False)
    
    # Birth details
    birth_weight = db.Column(db.Float)
    birth_length = db.Column(db.Float)
    birth_place = db.Column(db.String(100))
    birth_type = db.Column(db.String(50))  # Normal, Cesarean, etc.
    
    # Mother link (optional)
    mother_name = db.Column(db.String(120))
    mother_abha_id = db.Column(db.String(50))
    
    # Medical info
    blood_group = db.Column(db.String(5))
    allergies = db.Column(db.Text)
    medical_conditions = db.Column(db.Text)
    
    # Relationships
    checkups = db.relationship('Checkup', backref='child_record', lazy=True, cascade='all, delete-orphan')
    vaccinations = db.relationship('Vaccination', backref='child_record', lazy=True, cascade='all, delete-orphan')
    growth_metrics = db.relationship('GrowthMetric', backref='child_record', lazy=True, cascade='all, delete-orphan')
    
    # Tracking
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<ChildRecord {self.abha_id}>'


class Vaccination(db.Model):
    """Vaccination record"""
    __tablename__ = 'vaccinations'
    
    id = db.Column(db.Integer, primary_key=True)
    child_record_id = db.Column(db.Integer, db.ForeignKey('child_records.id'), nullable=False)
    
    vaccine_name = db.Column(db.String(100), nullable=False)
    scheduled_date = db.Column(db.Date)
    administered_date = db.Column(db.Date)
    status = db.Column(db.String(50))  # Pending, Completed, Missed, Overdue
    
    # Vaccine details
    lot_number = db.Column(db.String(50))
    expiry_date = db.Column(db.Date)
    site = db.Column(db.String(50))  # Injection site
    
    # Follow-up
    next_dose_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Vaccination {self.vaccine_name}>'


class GrowthMetric(db.Model):
    """Child growth tracking"""
    __tablename__ = 'growth_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    child_record_id = db.Column(db.Integer, db.ForeignKey('child_records.id'), nullable=False)
    
    measurement_date = db.Column(db.Date, nullable=False)
    age_months = db.Column(db.Integer)
    weight = db.Column(db.Float)  # in kg
    height = db.Column(db.Float)  # in cm
    head_circumference = db.Column(db.Float)  # in cm
    
    # Assessment
    weight_for_age = db.Column(db.String(50))  # Normal, Underweight, Overweight
    height_for_age = db.Column(db.String(50))
    notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GrowthMetric {self.measurement_date}>'


class Reminder(db.Model):
    """Health reminders and follow-ups"""
    __tablename__ = 'reminders'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    reminder_type = db.Column(db.String(50))  # Vaccination, Checkup, Delivery, etc.
    
    # Link to records
    maternal_record_id = db.Column(db.Integer, db.ForeignKey('maternal_records.id'))
    child_record_id = db.Column(db.Integer, db.ForeignKey('child_records.id'))
    
    # Scheduling
    due_date = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completed_date = db.Column(db.Date)
    
    # Urgency
    priority = db.Column(db.String(20))  # Low, Medium, High, Critical
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Reminder {self.title}>'


class Notification(db.Model):
    """System notifications"""
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text)
    notification_type = db.Column(db.String(50))  # Alert, Info, Success, Warning
    read = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Notification {self.title}>'
