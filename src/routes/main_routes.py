from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/services')
def services():
    return render_template('services.html')

@main_bp.route('/projects')
def projects():
    return render_template('projects.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

# Company data for templates
@main_bp.app_context_processor
def inject_company_data():
    return {
        'company_name': 'INTELECT MARINE',
        'company_tagline': 'Specialized Technical Workshop in Marine and Industrial Automation',
        'company_experience': '30+ years experience',
        'company_address': '8 Pontou street & Diogenous, Drapetsona 18648, Greece',
        'company_phone': '+30 210 4122261',
        'company_email': 'intelect@otenet.gr',
        'services': [
            'Automation D/G',
            'Automation M/E', 
            'Miscellaneous Automation Panel Manufacture',
            'Electrical and electronics (Automation)',
            'Boiler Automation',
            'P.L.C. Programming',
            'U.P.S. Systems',
            'Electronic Propulsion Control'
        ],
        'clients': [
            'LASKARIDIS GROUP',
            'GREEK NAVY',
            'MINOAN LINES (GRIMALDI GROUP)',
            'SEA JETS',
            'GENIMAR SHIPPING',
            'TSANGARIS BROS',
            'AEGEAN SEA LINES',
            'ASSO SUBSEA'
        ],
        'projects': [
            {
                'name': 'ΠΑΘ 050 Hellenic Coast Guard ship',
                'type': 'Coast Guard Vessel',
                'description': 'Complete automation system installation and maintenance for Hellenic Coast Guard patrol vessel.'
            },
            {
                'name': 'S/Y ΑΛΜΥΡΑ ΙΙ Perini 50m sailing yacht',
                'type': 'Luxury Sailing Yacht',
                'description': 'Advanced automation and control systems for 50-meter Perini Navi sailing yacht.'
            },
            {
                'name': 'ΠΓΥ ΑΤΛΑΣ Greek Navy support ship',
                'type': 'Naval Support Vessel',
                'description': 'Marine automation and electrical systems for Greek Navy support operations.'
            },
            {
                'name': 'ΠΓΥ ΠΕΡΣΕΑΣ Greek Navy support ship',
                'type': 'Naval Support Vessel', 
                'description': 'Comprehensive automation solutions for Greek Navy maritime operations.'
            }
        ]
    }

