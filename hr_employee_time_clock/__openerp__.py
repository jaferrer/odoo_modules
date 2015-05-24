{
    'name': "Employee time clock",
    'author': "Bytebrand GmbH",
	'summary': 'Track over- and undert-time, generate timesheets, upload public holidays',
    'website': "http://www.bytebrand.net",
    'category': 'Human Resources',
    'version': '1.0',
    'depends': ['hr_timesheet_sheet', 'hr_attendance', 'hr_contract'],
	'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views.xml',
        'wizard/create_timesheet_with_tag_view.xml', # View file for the wizard
    ]
}