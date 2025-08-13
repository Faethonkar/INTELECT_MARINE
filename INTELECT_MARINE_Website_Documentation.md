# INTELECT MARINE Website Documentation

## Project Overview

A modern, interactive website for INTELECT MARINE company featuring Python backend logic and motion animations. The website showcases the company's marine and industrial automation services with a professional, responsive design.

## Live Website

**URL:** https://mzhyi8cdyn9g.manus.space

## Features Implemented

### 1. Modern Design & User Experience
- **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- **Modern Typography**: Uses Inter and Orbitron fonts for professional appearance
- **Color Scheme**: Professional blue gradient theme reflecting marine industry
- **Loading Animation**: Smooth loading screen with spinner animation
- **Smooth Scrolling**: Enhanced navigation with smooth scrolling effects

### 2. Interactive Animations & Motion Effects
- **Hero Section Animations**: Staggered fade-in animations for title, subtitle, and call-to-action
- **Animated Statistics**: Counter animations that trigger when scrolling into view
- **Card Hover Effects**: Smooth hover transitions with elevation and glow effects
- **Intersection Observer**: Elements animate into view as user scrolls
- **Navbar Scroll Effects**: Dynamic navbar that changes appearance on scroll
- **Button Animations**: Interactive buttons with hover and click effects

### 3. Python Backend Logic (Flask)
- **Contact Form Processing**: Functional contact form with Python backend validation
- **API Endpoints**: RESTful API for form submissions (`/api/contact`)
- **Data Management**: Structured data handling for company information and projects
- **Template Rendering**: Dynamic content rendering using Jinja2 templates
- **Error Handling**: Proper error handling and user feedback

### 4. Website Pages

#### Homepage (`/`)
- Hero section with company introduction
- Animated statistics (30+ years experience, 500+ projects, ISO certification)
- Services overview with interactive cards
- About section with company story
- Client showcase
- Call-to-action section

#### Services Page (`/services`)
- Detailed service descriptions with feature lists
- Interactive service cards with hover effects
- Comprehensive coverage of all automation services:
  - Marine Engine Automation
  - PLC Programming
  - Panel Manufacturing
  - UPS Systems
  - Boiler Automation
  - Electronic Propulsion Control

#### Projects Page (`/projects`)
- Project showcase with real ship images
- Featured projects including:
  - ΠΑΘ 050 Hellenic Coast Guard ship
  - S/Y ΑΛΜΥΡΑ ΙΙ Perini 50m sailing yacht
  - ΠΓΥ ΑΤΛΑΣ Greek Navy support ship
  - ΠΓΥ ΠΕΡΣΕΑΣ Greek Navy support ship
- Project statistics with animated counters
- Vessel types served section

#### About Page (`/about`)
- Company history and foundation story
- Team member profiles
- Certifications and standards
- Company values and mission
- Professional imagery

#### Contact Page (`/contact`)
- Functional contact form with Python backend
- Company contact information
- Business hours
- Emergency support details
- Interactive form validation
- Success/error message handling

### 5. Technical Implementation

#### Frontend Technologies
- **HTML5**: Semantic markup structure
- **CSS3**: Advanced styling with animations and transitions
- **JavaScript**: Interactive functionality and form handling
- **Font Awesome**: Professional icons throughout the site
- **Google Fonts**: Typography enhancement

#### Backend Technologies
- **Flask**: Python web framework
- **Jinja2**: Template engine for dynamic content
- **SQLAlchemy**: Database ORM (configured but not actively used)
- **JSON API**: RESTful API endpoints

#### Assets & Media
- **High-Quality Images**: Professional marine automation and ship images
- **Optimized Graphics**: Properly sized and compressed images
- **Icon Integration**: Consistent iconography throughout

### 6. Performance & Optimization
- **Fast Loading**: Optimized images and efficient CSS/JS
- **Smooth Animations**: Hardware-accelerated CSS animations
- **Mobile Performance**: Optimized for mobile devices
- **SEO-Friendly**: Proper meta tags and semantic HTML

### 7. Security & Best Practices
- **Form Validation**: Both client-side and server-side validation
- **Error Handling**: Graceful error handling and user feedback
- **CORS Support**: Proper cross-origin request handling
- **Input Sanitization**: Safe handling of user input

## Company Information Integrated

### Services Offered
- Automation D/G (Diesel Generator)
- Automation M/E (Main Engine)
- Miscellaneous Automation Panel Manufacture
- Electrical and electronics (Automation)
- Boiler Automation
- P.L.C. Programming
- U.P.S. Systems
- Electronic Propulsion Control

### Major Clients
- LASKARIDIS GROUP
- GREEK NAVY
- MINOAN LINES (GRIMALDI GROUP)
- SEA JETS
- GENIMAR SHIPPING
- TSANGARIS BROS
- AEGEAN SEA LINES
- ASSO SUBSEA

### Contact Information
- **Address**: 8 Pontou street & Diogenous, Drapetsona 18648, Greece
- **Phone**: +30 210 4122261
- **Email**: intelect@otenet.gr
- **Certification**: BUREAU VERITAS ISO 9001

## Technical Architecture

### File Structure
```
intelect_marine/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── main_routes.py      # Main website routes
│   │   └── user.py             # User-related routes
│   ├── templates/
│   │   ├── base.html           # Base template with navigation
│   │   ├── index.html          # Homepage
│   │   ├── services.html       # Services page
│   │   ├── projects.html       # Projects page
│   │   ├── about.html          # About page
│   │   └── contact.html        # Contact page
│   ├── static/
│   │   └── images/             # Website images
│   └── models/
│       └── user.py             # Database models
├── requirements.txt            # Python dependencies
└── venv/                       # Virtual environment
```

### API Endpoints
- `GET /` - Homepage
- `GET /services` - Services page
- `GET /projects` - Projects page
- `GET /about` - About page
- `GET /contact` - Contact page
- `POST /api/contact` - Contact form submission

## Browser Compatibility
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancement Opportunities
1. **Database Integration**: Store contact form submissions
2. **Admin Panel**: Content management system
3. **Multi-language Support**: Greek and English versions
4. **Blog Section**: Industry news and updates
5. **Project Gallery**: Expanded project showcase
6. **Client Portal**: Secure client access area
7. **Live Chat**: Real-time customer support
8. **Analytics Integration**: Google Analytics tracking

## Maintenance Notes
- Images are stored in `/src/static/images/`
- Contact form submissions are currently logged to console
- All animations are CSS-based for optimal performance
- Website is fully responsive and mobile-optimized
- Flask application runs on port 5001 locally

## Deployment Information
- **Platform**: Manus deployment service
- **URL**: https://mzhyi8cdyn9g.manus.space
- **Framework**: Flask (Python)
- **Status**: Production-ready and fully functional

The website successfully combines modern web design principles with functional Python backend logic, creating a professional online presence for INTELECT MARINE that effectively showcases their marine automation expertise and services.

