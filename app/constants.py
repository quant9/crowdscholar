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

# U.S. states
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

#
CATEGORIES = [
(0, 'General'),
(1, 'Athletic'),
(2, 'Community & Local'),
(3, 'Academics (General)'),
(4, 'Art & Fashion'),
(5, 'Music & Performance'),
(6, 'Science & Technology'),
(7, 'Business & Entrepreneurship'),
(8, 'Vocational / Professional'),
(9, 'Essay & Other Competitions'),
]

AFFILIATIONS = [
(0, 'General / None'),
(1, 'Ethnic Group'),
(2, 'Religious Group'),
(3, 'Military / Veteran'),
(4, 'Political Organization'),
(5, 'Disabled & Special Needs'),
(6, 'Employer Affiliation'),
(7, 'Nonprofit Organization / Foundation'),
(8, 'Interest / Hobby Group'),
(9, 'Other Affiliation'),
]

    undergrad_not_enrolled = BooleanField('High School graduate not enrolled in college')
    undergrad_enrolled = BooleanField('Current college student')
    postgrad_not_enrolled = BooleanField('Prospective graduate student')
    postgrad_enrolled = BooleanField('Current graduate student')













