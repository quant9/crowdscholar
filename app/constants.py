# user role
ADMIN = 0
STUDENT = 1
DONOR = 2
OTHERUSER = 3
USERTYPE = {
    ADMIN: 'admin',
    STUDENT: 'student',
    DONOR: 'donor',
    OTHERUSER: 'other',
}

# user status
INACTIVE = 0
NEW = 1
ACTIVE = 2
STATUS = {
    INACTIVE: 'inactive',
    NEW: 'new',
    ACTIVE: 'active',
}

# scholarship status
FUNDING = 0
READY = 1
PAID_OUT = 2
EXPIRED = 3
WITHDRAWN = 4
SCHOLARSHIP_STATUS = {
    FUNDING: 'in funding',
    READY: 'fully funded',
    PAID_OUT: 'paid out',
    EXPIRED: 'expired',
    WITHDRAWN: 'withdrawn',
    }

STATES = [('Alabama', 'Alabama'),
('Alaska', 'Alaska'),
('Arizona', 'Arizona'),
('Arkansas', 'Arkansas'),
('California', 'California'),
('Colorado', 'Colorado'),
('Connecticut', 'Connecticut'),
('Delaware', 'Delaware'),
('Florida', 'Florida'),
('Georgia', 'Georgia'),
('Hawaii', 'Hawaii'),
('Idaho', 'Idaho'),
('Illinois', 'Illinois'),
('Indiana', 'Indiana'),
('Iowa', 'Iowa'),
('Kansas', 'Kansas'),
('Kentucky', 'Kentucky'),
('Louisiana', 'Louisiana'),
('Maine', 'Maine'),
('Maryland', 'Maryland'),
('Massachusetts', 'Massachusetts'),
('Michigan', 'Michigan'),
('Minnesota', 'Minnesota'),
('Mississippi', 'Mississippi'),
('Missouri', 'Missouri'),
('Montana', 'Montana'),
('Nebraska', 'Nebraska'),
('Nevada', 'Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio', 'Ohio'),
('Oklahoma', 'Oklahoma'),
('Oregon', 'Oregon'),
('Pennsylvania', 'Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee', 'Tennessee'),
('Texas', 'Texas'),
('Utah', 'Utah'),
('Vermont', 'Vermont'),
('Virginia', 'Virginia'),
('Washington', 'Washington'),
('West Virginia', 'West Virginia'),
('Wisconsin', 'Wisconsin'),
('Wyoming', 'Wyoming'),
('American Samoa', 'American Samoa'),
('District of Columbia', 'District of Columbia'),
('Guam', 'Guam'),
('Marshall Islands', 'Marshall Islands'),
('Northern Mariana Islands', 'Northern Mariana Islands'),
('Palau', 'Palau'),
('Puerto Rico', 'Puerto Rico'),
('Virgin Islands', 'Virgin Islands'),
]