# 💻 Robert Macatiag | Personal Portfolio

A modern, responsive personal portfolio website built with **Streamlit** featuring a sleek dark tech aesthetic with terminal-inspired design. Showcasing projects, certificates, professional experience, and contact information with smooth animations and clean UI/UX.

---

## 📁 Folder Structure

```
bert/act2/
│
├── 📄 Home.py                    # Main entry point / Home page
├── 📄 sidebar.py                 # Shared sidebar styling & components
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # Project documentation
│
├── 📂 pages/                     # Streamlit multi-page app pages
│   ├── 1_About.py               # About Me & Professional Info
│   ├── 2_Projects.py            # Projects showcase & portfolio
│   ├── 3_Certificate.py         # Certifications & achievements
│   └── 4_Contact.py             # Contact form & information
│
└── 📂 assets/                    # Static assets
    ├── 📂 profiles/             # Profile images
    │   └── profile.png
    │
    ├── 📂 projects/             # Project screenshots
    │   ├── project1.png
    │   ├── project2.png
    │   └── ...
    │
    └── 📂 certificate/          # Certificate images
        ├── cert1.png
        └── cert2.png
```

---

## 🎨 Design System

### Color Palette (Terminal Theme)

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Neon Green** | `#00FF41` | Primary accents, headings, hover states |
| **Orange** | `#FF6B00` | Secondary accents, icons, highlights |
| **Sky Blue** | `#4A9EFF` | Tertiary accents, badges, links |
| **Dark BG** | `#030703` | Main background |
| **Card BG** | `#050C05` | Card backgrounds |
| **Border** | `#152515` | Borders, dividers |
| **Light Green** | `#2A5A2A` | Secondary text |
| **Light Text** | `#C8D8C8` | Primary text |
| **White** | `#E8F5E9` | Headings, highlights |

### Key Design Elements

- **Terminal Aesthetic**: Matrix-like scanline overlays, green text on dark backgrounds
- **Clip-path Polygons**: Angular geometric shapes for modern look
- **Hover Animations**: Scale transformations and shadow effects
- **Grid Background**: Subtle repeating patterns
- **Gradient Accents**: Orange to green gradients for visual depth

### Typography

| Element | Font Family | Size | Weight |
|---------|-------------|------|--------|
| **Headings** | Black Ops One | 2rem - 3.5rem | 400 |
| **Subheadings** | Barlow Condensed | 1.2rem - 1.8rem | 600-700 |
| **Monospace** | JetBrains Mono | 0.72rem - 1rem | 300-800 |
| **Body Text** | JetBrains Mono | 0.8rem - 0.9rem | 400 |

---

## ✨ Features

### 🏠 Home Page
- Hero section with professional introduction
- Profile image with neon glow effects
- Call-to-action navigation buttons
- Social media links (GitHub, LinkedIn, Email, etc.)
- Responsive layout with terminal aesthetic

### 👤 About Page
- Professional background and biography
- Skills and expertise showcase
- Education and certifications summary
- Experience highlights
- Clean, scanline-enhanced design

### 💻 Projects Page
- Project portfolio grid layout
- Project cards with images and descriptions
- Technology stack badges for each project
- Project links and call-to-action buttons
- Hover effects with scale animations
- Project statistics dashboard

### 🏆 Certificates Page
- Certificate gallery with full image previews
- Base64-encoded image display (works in all environments)
- Certificate details: issuer, date, and badge
- Learning journey statistics
- Interactive card hover effects
- Terminal-styled achievement showcase
- Stats include: Total Certifications, Years of Learning, Hours of Study, Platforms Used

### 📧 Contact Page
- Contact form with validation
- Social media links and contact details
- Professional information display
- Responsive design for all devices

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to the project folder**:
```bash
cd bert/act2
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
streamlit run Home.py
```

4. **Open in browser**:
The application will automatically open at `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit>=1.28.0
Pillow>=10.0.0
```

See `requirements.txt` for complete dependency list.

---

## 📱 Responsive Design

The portfolio is fully responsive with breakpoints at:
- **Desktop**: > 992px (Full layout, optimized spacing)
- **Tablet**: 600px - 992px (Adjusted grid, 2-column layouts)
- **Mobile**: < 600px (Single column, stacked layout)

### Mobile Optimizations:
- Stacked layouts for all pages
- Full-width images and cards
- Touch-friendly interactions
- Adjusted font sizes for readability
- Optimized spacing and padding

---

## 🎯 Design & Technical Highlights

1. **Modern Terminal Aesthetic**: Green neon text on dark backgrounds for a tech-forward look
2. **Geometric Design**: Angular clip-path shapes and scanline overlays
3. **Smooth Animations**: Scale, translate, and opacity transitions on hover
4. **Base64 Image Encoding**: Certificate images embedded as data URIs for reliable display
5. **Consistent Visual Language**: Unified color scheme and typography across all pages
6. **Dark Mode**: Eye-friendly dark theme throughout
7. **Clean Code Structure**: Modular design with shared sidebar styling

---

## 🔧 Technical Implementation

### Key Technologies
- **Streamlit**: Multi-page app framework
- **Python**: Backend logic and data handling
- **CSS/HTML**: Custom styling with Streamlit markdown
- **Base64 Encoding**: Image display in HTML contexts

### File Organization
- `sidebar.py`: Reusable sidebar styling and components
- `Home.py`: Main entry point
- `pages/`: Individual page implementations
- `assets/`: Static images and resources

---

## 📝 Recent Updates

- ✅ Fixed certificate image display with base64 encoding
- ✅ Updated folder structure documentation
- ✅ Implemented terminal/neon design theme
- ✅ Added learning journey statistics section
- ✅ Enhanced responsive design

---

## 📄 License

This portfolio is created and maintained by **Robert Macatiag** © 2026.

---

## 🚀 Future Enhancements

- Dark/Light mode toggle
- Blog section
- Video resume feature
- Interactive project demos
- Real-time GitHub stats integration

---

**Built with ⚡ by Robert Macatiag**
6. **Image-First Design**: Galleries and cards prioritize visual content

---

## 🔧 Customization

### Adding New Projects
Edit `pages/3_Projects.py` and add to the `projects_data` list:
```python
{
    'file': 'p6.png',
    'title': 'New Project',
    'description': 'Project description here.',
    'tech': ['Python', 'React', 'API'],
    'github': 'https://github.com/username/repo',
    'demo': 'https://demo-link.com'
}
```

### Adding New Certificates
Edit `pages/4_Certificate.py` and add to the `certificates` list:
```python
{
    'name': 'Certificate Name',
    'issuer': 'Issuing Organization',
    'date': '2024',
    'badge': 'Category',
    'icon': 'svg-path-data',
    'image': 'cert4.png'
}
```

### Changing Colors
Edit the CSS in any page file to update the color scheme. Main colors are defined in the `:root` or as CSS variables.

---

## 📄 License

This project is created for personal portfolio use by **Ma. Bea Belasa**.

---

## 👩‍💻 Author

**Ma. Bea Belasa**
- 3rd Year Computer Science Student
- Passionate about web development and design
- Building the future, one project at a time ✨

---

## 🤝 Connect

- 📧 Email: mabeabelasa@email.com
- 💼 LinkedIn: linkedin.com/in/mabeabelasa
- 🐙 GitHub: github.com/mabeabelasa
- 🌐 Facebook: facebook.com/Missbea070322

---

Made with 💖 using Streamlit | © 2024 Ma. Bea Belasa
