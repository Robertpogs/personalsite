import streamlit as st
import os
import base64
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sidebar import apply_sidebar_styles, render_sidebar

def get_image_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(
    page_title='Projects | Robert Macatiag',
    page_icon='💻',
    layout='wide'
)

apply_sidebar_styles()

st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Black+Ops+One&display=swap');

/* ─── Reset & Global ─────────────────────────────────── */
* { box-sizing: border-box; margin: 0; padding: 0; }

.main {
    background:
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 40px,
            rgba(0, 255, 65, 0.015) 40px,
            rgba(0, 255, 65, 0.015) 41px
        ),
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 40px,
            rgba(0, 255, 65, 0.015) 40px,
            rgba(0, 255, 65, 0.015) 41px
        ),
        linear-gradient(180deg, #050A05 0%, #070D0A 40%, #050A08 70%, #030703 100%);
    min-height: 100vh;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1400px !important;
}

/* ─── Scanline overlay ───────────────────────────────── */
.main::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.03) 0px,
        rgba(0, 0, 0, 0.03) 1px,
        transparent 1px,
        transparent 3px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ─── SCROLLBAR ──────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #030703; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #1A3A1A, #0D1F0D);
    border-radius: 0;
}
::-webkit-scrollbar-thumb:hover { background: #00FF41; }

/* ─── PAGE HEADER ────────────────────────────────────── */
.page-header {
    padding: 1rem 0.5rem 2rem;
    position: relative;
}

.page-header-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00FF41;
    padding: 0.4rem 1rem;
    border: 1px solid #1A3A1A;
    background: rgba(0,255,65,0.03);
    margin-bottom: 1rem;
    clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
}

.page-header-badge::before {
    content: '$';
    color: #FF6B00;
    font-weight: 800;
}

.page-main-title {
    font-family: 'Black Ops One', cursive;
    font-size: 3.5rem;
    font-weight: 400;
    color: #E8F5E9;
    margin-bottom: 0.3rem;
    line-height: 1.1;
    letter-spacing: 3px;
    text-shadow:
        0 0 40px rgba(0, 255, 65, 0.15),
        2px 2px 0px #1A2A1A,
        4px 4px 0px #0D180D;
}

.page-main-title span {
    color: #00FF41;
    text-shadow:
        0 0 20px rgba(0,255,65,0.4),
        2px 2px 0px #0A1A0A;
}

.title-underline {
    width: 260px;
    height: 4px;
    background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 30%, #00FF41 60%, transparent 100%);
    margin-bottom: 1rem;
    clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
}

.page-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #2A5A2A;
    letter-spacing: 2px;
}

.page-subtitle::before {
    content: '// ';
    color: #FF6B00;
}

/* ─── SECTION HEADER ─────────────────────────────────── */
.section-header {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 2rem;
    padding: 0 0.5rem;
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1A3A1A, transparent);
}

.section-line-rev {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1A3A1A);
}

.section-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #00FF41;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border: 1px solid #1A3A1A;
    background: rgba(0,255,65,0.03);
    white-space: nowrap;
}

/* ─── PROJECT CARD ───────────────────────────────────── */
.project-card {
    background: rgba(5, 12, 5, 0.95);
    border: 1px solid #152515;
    border-top: 3px solid #00FF41;
    overflow: hidden;
    transition: all 0.42s ease;
    margin-bottom: 1.8rem;
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
    clip-path: polygon(
        0 0,
        calc(100% - 16px) 0,
        100% 16px,
        100% 100%,
        16px 100%,
        0 calc(100% - 16px)
    );
}

/* Corner accent */
.project-card::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 16px; height: 16px;
    background: #00FF41;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.4;
    transition: opacity 0.3s ease;
    z-index: 5;
}

.project-card:hover::after { opacity: 1; }

.project-card:hover {
    transform: translateY(-8px);
    border-color: #2A4A2A;
    border-top-color: #00FF41;
    box-shadow:
        0 16px 48px rgba(0,255,65,0.12),
        0 0 0 1px rgba(0,255,65,0.15);
}

/* Card variants */
.project-card-orange {
    border-top-color: #FF6B00 !important;
}

.project-card-orange::after {
    background: #FF6B00 !important;
}

.project-card-orange:hover {
    box-shadow:
        0 16px 48px rgba(255,107,0,0.12),
        0 0 0 1px rgba(255,107,0,0.15) !important;
}

.project-card-blue {
    border-top-color: #4A9EFF !important;
}

.project-card-blue::after {
    background: #4A9EFF !important;
}

.project-card-blue:hover {
    box-shadow:
        0 16px 48px rgba(74,158,255,0.12),
        0 0 0 1px rgba(74,158,255,0.15) !important;
}

/* ─── PROJECT IMAGE ──────────────────────────────────── */
.project-image-wrapper {
    width: 100%;
    height: 220px;
    overflow: hidden;
    background: linear-gradient(145deg, #0A1A0A, #050A05);
    position: relative;
}

.project-image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
    transition: transform 0.55s ease;
    filter: contrast(1.05) saturate(0.85);
}

.project-card:hover .project-image-wrapper img {
    transform: scale(1.08);
}

/* Scan line on image hover */
.project-image-wrapper::after {
    content: '';
    position: absolute;
    left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(0,255,65,0.6), transparent);
    top: -10%;
    transition: top 0.6s ease;
    pointer-events: none;
    z-index: 3;
}

.project-card:hover .project-image-wrapper::after {
    top: 110%;
}

/* Image overlay */
.project-image-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to top,
        rgba(5,10,5,0.92) 0%,
        rgba(5,10,5,0.5) 40%,
        transparent 75%
    );
    opacity: 0;
    transition: opacity 0.38s ease;
    display: flex;
    align-items: flex-end;
    padding: 1rem;
    z-index: 2;
}

.project-card:hover .project-image-overlay {
    opacity: 1;
}

.project-overlay-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(0,255,65,0.1);
    border: 1px solid rgba(0,255,65,0.4);
    color: #00FF41;
    padding: 0.35rem 0.9rem;
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

/* Placeholder */
.project-placeholder {
    width: 100%;
    height: 220px;
    background: linear-gradient(145deg, #080F08, #0A1A0A, #0F200F);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    border-bottom: 1px solid #1A3A1A;
    position: relative;
}

.project-placeholder::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 20px,
        rgba(0,255,65,0.015) 20px,
        rgba(0,255,65,0.015) 21px
    );
}

.project-placeholder-letter {
    font-family: 'Black Ops One', cursive;
    font-size: 4rem;
    color: #1A3A1A;
    letter-spacing: 4px;
    line-height: 1;
    position: relative;
    z-index: 1;
}

.project-placeholder-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #00FF41;
    letter-spacing: 4px;
    text-transform: uppercase;
    position: relative;
    z-index: 1;
}

/* ─── CARD BODY ──────────────────────────────────────── */
.project-content {
    padding: 1.4rem 1.6rem 1.6rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    position: relative;
}

.project-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #2A4A2A;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.project-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #C8D8C8;
    margin: 0 0 0.6rem 0;
    line-height: 1.2;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.project-description {
    font-family: 'JetBrains Mono', monospace;
    color: #3A5A3A;
    font-size: 0.82rem;
    line-height: 1.9;
    margin: 0 0 1.2rem 0;
    flex-grow: 1;
    padding: 0.8rem 1rem;
    background: rgba(0,255,65,0.02);
    border: 1px solid #1A2E1A;
    border-left: 2px solid #2A4A2A;
    position: relative;
}

.project-description::before {
    content: '// DESC';
    position: absolute;
    top: -9px; left: 8px;
    font-size: 0.62rem;
    color: #00FF41;
    background: #050A05;
    padding: 0 5px;
    letter-spacing: 2px;
    font-family: 'JetBrains Mono', monospace;
}

/* ─── TECH TAGS ──────────────────────────────────────── */
.tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.2rem;
}

.tech-tag {
    display: inline-block;
    background: transparent;
    color: #00FF41;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1px;
    padding: 0.3rem 0.8rem;
    border: 1px solid #1E3D1E;
    text-transform: uppercase;
    transition: all 0.25s ease;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    cursor: default;
}

.tech-tag::before {
    content: '#';
    color: #FF6B00;
    margin-right: 3px;
}

.tech-tag:hover {
    background: rgba(0,255,65,0.08);
    border-color: #00FF41;
    box-shadow: 0 0 10px rgba(0,255,65,0.15);
    transform: translateY(-2px);
}

/* ─── PROJECT LINKS ──────────────────────────────────── */
.project-links {
    display: flex;
    gap: 0.7rem;
    flex-wrap: wrap;
}

.project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    color: #2A5A2A;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 0.5rem 1rem;
    background: transparent;
    border: 1px solid #1E3D1E;
    transition: all 0.3s ease;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.project-link:hover {
    background: rgba(0,255,65,0.08);
    color: #00FF41;
    border-color: #00FF41;
    box-shadow: 0 0 14px rgba(0,255,65,0.18);
    transform: translateY(-2px);
    text-decoration: none;
}

.project-link-demo:hover {
    background: rgba(255,107,0,0.08) !important;
    color: #FF6B00 !important;
    border-color: #FF6B00 !important;
    box-shadow: 0 0 14px rgba(255,107,0,0.18) !important;
}

/* ─── STATS SECTION ──────────────────────────────────── */
.stats-section {
    background: rgba(5, 12, 5, 0.95);
    border: 1px solid #152515;
    padding: 2.5rem 2rem;
    margin-top: 1rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    clip-path: polygon(
        0 0,
        calc(100% - 20px) 0,
        100% 20px,
        100% 100%,
        20px 100%,
        0 calc(100% - 20px)
    );
}

/* Corner accent */
.stats-section::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 20px; height: 20px;
    background: #00FF41;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.3;
}

.stats-section::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 20px; height: 20px;
    background: #FF6B00;
    clip-path: polygon(0 0, 0 100%, 100% 100%);
    opacity: 0.3;
}

.stats-title {
    font-family: 'Black Ops One', cursive;
    font-size: 2rem;
    font-weight: 400;
    color: #E8F5E9;
    margin-bottom: 0.3rem;
    text-align: center;
    letter-spacing: 3px;
    text-shadow: 0 0 30px rgba(0,255,65,0.1);
}

.stats-title span { color: #00FF41; }

.stats-divider {
    width: 80px; height: 3px;
    background: linear-gradient(90deg, #FF6B00, #00FF41);
    margin: 0.5rem auto 2rem;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1.2rem;
}

.stat-item {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid #1A3A1A;
    padding: 1.8rem 1rem;
    text-align: center;
    transition: all 0.35s ease;
    position: relative;
    clip-path: polygon(
        0 0,
        calc(100% - 12px) 0,
        100% 12px,
        100% 100%,
        12px 100%,
        0 calc(100% - 12px)
    );
}

.stat-item::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 12px; height: 12px;
    background: #1A3A1A;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
}

.stat-item:hover {
    transform: translateY(-6px);
    border-color: #2A5A2A;
    box-shadow: 0 12px 36px rgba(0,255,65,0.1);
}

.stat-icon-container {
    width: 52px; height: 52px;
    background: rgba(0,255,65,0.08);
    border: 1px solid #1E3D1E;
    margin: 0 auto 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    transition: all 0.3s ease;
}

.stat-item:hover .stat-icon-container {
    background: rgba(0,255,65,0.12);
    border-color: #00FF41;
    box-shadow: 0 0 16px rgba(0,255,65,0.15);
}

.stat-icon-orange {
    background: rgba(255,107,0,0.08) !important;
    border-color: #3D2000 !important;
}

.stat-item:hover .stat-icon-orange {
    background: rgba(255,107,0,0.12) !important;
    border-color: #FF6B00 !important;
    box-shadow: 0 0 16px rgba(255,107,0,0.15) !important;
}

.stat-icon-blue {
    background: rgba(74,158,255,0.08) !important;
    border-color: #001A3D !important;
}

.stat-item:hover .stat-icon-blue {
    background: rgba(74,158,255,0.12) !important;
    border-color: #4A9EFF !important;
    box-shadow: 0 0 16px rgba(74,158,255,0.15) !important;
}

.stat-icon-purple {
    background: rgba(221,160,221,0.08) !important;
    border-color: #2A1A2A !important;
}

.stat-item:hover .stat-icon-purple {
    background: rgba(221,160,221,0.12) !important;
    border-color: #DDA0DD !important;
    box-shadow: 0 0 16px rgba(221,160,221,0.15) !important;
}

.stat-number {
    font-family: 'Black Ops One', cursive;
    font-size: 2.4rem;
    color: #00FF41;
    line-height: 1;
    margin: 0 0 0.4rem 0;
    text-shadow: 0 0 20px rgba(0,255,65,0.3);
    letter-spacing: 2px;
}

.stat-number-orange { color: #FF6B00 !important; text-shadow: 0 0 20px rgba(255,107,0,0.3) !important; }
.stat-number-blue   { color: #4A9EFF !important; text-shadow: 0 0 20px rgba(74,158,255,0.3) !important; }
.stat-number-purple { color: #DDA0DD !important; text-shadow: 0 0 20px rgba(221,160,221,0.3) !important; }

.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #2A5A2A;
    font-weight: 400;
    margin: 0;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ─── FOOTER ─────────────────────────────────────────── */
.footer {
    background: #030703;
    border-top: 1px solid #1A3A1A;
    padding: 2.5rem 2rem;
    margin-top: 4rem;
    margin-bottom: -5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.footer::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00FF41, #FF6B00, #00FF41, transparent);
    background-size: 200% auto;
    animation: shimmer 4s linear infinite;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.footer-content { max-width: 800px; margin: 0 auto; }

.footer-name {
    font-family: 'Black Ops One', cursive;
    font-size: 1.8rem;
    color: #C8D8C8;
    margin-bottom: 0.3rem;
    letter-spacing: 4px;
    text-shadow: 0 0 30px rgba(0,255,65,0.1);
}

.footer-tagline {
    font-family: 'JetBrains Mono', monospace;
    color: #2A5A2A;
    font-size: 0.8rem;
    margin-bottom: 1.5rem;
    letter-spacing: 2px;
}

.footer-divider {
    width: 80px; height: 2px;
    background: linear-gradient(90deg, #FF6B00, #00FF41);
    margin: 0 auto 1.5rem;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.footer-copyright {
    font-family: 'JetBrains Mono', monospace;
    color: #1E3D1E;
    font-size: 0.78rem;
    letter-spacing: 2px;
}

.footer-heart { color: #FF6B00; }

/* ─── MOBILE ─────────────────────────────────────────── */
@media screen and (max-width: 992px) {
    .page-main-title { font-size: 2.5rem; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .block-container {
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }
    .project-image-wrapper { height: 200px; }
}

@media screen and (max-width: 768px) {
    .project-image-wrapper { height: 180px; }
    .project-content { padding: 1.2rem; }
    .project-title { font-size: 1.1rem; }
}

@media screen and (max-width: 600px) {
    .page-main-title { font-size: 2rem; }
    .stats-section { padding: 1.8rem 1.2rem; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 1rem; }
    .project-image-wrapper { height: 160px; }
    .tech-tag { font-size: 0.68rem; }
    .project-link { font-size: 0.7rem; padding: 0.4rem 0.8rem; }
}

@media screen and (max-width: 480px) {
    .project-image-wrapper { height: 150px; }
    .stats-grid { grid-template-columns: 1fr; }
    .page-header-badge { font-size: 0.7rem; }
}
</style>
''', unsafe_allow_html=True)

# ── Projects Data ─────────────────────────────────────────────────────────────
projects_data = [
    {
        'file': 'p1.png',
        'title': 'Herblux SkinCare & Product System',
        'description': 'A full-stack e-commerce solution with user authentication, product management, and secure payment integration.',
        'tech': ['PHP', 'MySQL', 'HTML/CSS'],
        'github': 'https://github.com',
        'demo': '#',
        'color': 'green'
    },
    {
        'file': 'p2.png',
        'title': 'Port',
        'description': 'Customize port using html,css,js',
        'tech': ['Html', 'CSS', 'js'],
        'github': '#',
        'demo': '#',
        'color': 'orange'
    },
    {
        'file': 'p3.png',
        'title': 'Gamified Port',
        'description': 'Gamified game using react js, js, other lib',
        'tech': ['js', 'React'],
        'github': '#',
        'demo': '#',
        'color': 'blue'
    },
]

# ── Page Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-badge">ls ./projects --all</div>
    <h1 class="page-main-title">My <span>Projects</span></h1>
    <div class="title-underline"></div>
    <p class="page-subtitle">building solutions, one line of code at a time</p>
</div>
""", unsafe_allow_html=True)

# ── Section divider ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// Deployed Modules</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

# ── Projects Grid ─────────────────────────────────────────────────────────────
color_map = {
    'green': '',
    'orange': 'project-card-orange',
    'blue': 'project-card-blue'
}

cols_per_row = 3
for i in range(0, len(projects_data), cols_per_row):
    row_projects = projects_data[i:i + cols_per_row]
    cols = st.columns(len(row_projects))

    for idx, (col, project) in enumerate(zip(cols, row_projects)):
        with col:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(
                current_dir, '..', 'assets', 'projects', project['file']
            )
            img_path = os.path.normpath(img_path)
            img_exists = os.path.exists(img_path)

            tech_tags_html = ''.join([
                f'<span class="tech-tag">{tech}</span>'
                for tech in project['tech']
            ])

            card_class = f"project-card {color_map.get(project['color'], '')}"
            proj_num   = f"PROJECT_{str(i + idx + 1).zfill(2)}"

            st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)

            # Image / Placeholder
            if img_exists:
                with open(img_path, 'rb') as img_file:
                    img_b64 = base64.b64encode(img_file.read()).decode()
                ext = project['file'].split('.')[-1].lower()
                mime = 'jpeg' if ext in ('jpg', 'jpeg') else 'png'
                st.markdown(f'''
                <div class="project-image-wrapper">
                    <img src="data:image/{mime};base64,{img_b64}"
                         alt="{project['title']}">
                    <div class="project-image-overlay">
                        <span class="project-overlay-tag">
                            &gt; VIEW_PROJECT
                        </span>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                <div class="project-placeholder">
                    <div class="project-placeholder-letter">
                        {project["title"][0]}
                    </div>
                    <div class="project-placeholder-sub">&gt; NO_PREVIEW</div>
                </div>
                ''', unsafe_allow_html=True)

            # Card content
            st.markdown(f'''
            <div class="project-content">
                <div class="project-num">{proj_num}</div>
                <h3 class="project-title">{project["title"]}</h3>
                <p class="project-description">{project["description"]}</p>
                <div class="tech-tags">{tech_tags_html}</div>
                <div class="project-links">
                    <a href="{project["github"]}" class="project-link"
                       target="_blank">
                        <svg width="14" height="14" viewBox="0 0 24 24"
                             fill="none" stroke="currentColor"
                             stroke-width="2" stroke-linecap="round"
                             stroke-linejoin="round">
                            <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87
                                     a3.37 3.37 0 0 0-.94-2.61
                                     c3.14-.35 6.44-1.54 6.44-7
                                     A5.44 5.44 0 0 0 20 4.77
                                     5.07 5.07 0 0 0 19.91 1
                                     S18.73.65 16 2.48
                                     a13.38 13.38 0 0 0-7 0
                                     C6.27.65 5.09 1 5.09 1
                                     A5.07 5.07 0 0 0 5 4.77
                                     a5.44 5.44 0 0 0-1.5 3.78
                                     c0 5.42 3.3 6.61 6.44 7
                                     A3.37 3.37 0 0 0 9 18.13V22"/>
                        </svg>
                        GITHUB
                    </a>
                    <a href="{project["demo"]}"
                       class="project-link project-link-demo"
                       target="_blank">
                        <svg width="14" height="14" viewBox="0 0 24 24"
                             fill="none" stroke="currentColor"
                             stroke-width="2" stroke-linecap="round"
                             stroke-linejoin="round">
                            <path d="M18 13v6a2 2 0 0 1-2 2H5
                                     a2 2 0 0 1-2-2V8
                                     a2 2 0 0 1 2-2h6"/>
                            <polyline points="15 3 21 3 21 9"/>
                            <line x1="10" y1="14" x2="21" y2="3"/>
                        </svg>
                        LIVE_DEMO
                    </a>
                </div>
            </div>
            </div>
            ''', unsafe_allow_html=True)

# ── Stats Section ─────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// System Stats</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stats-section">
    <h2 class="stats-title">Project <span>Statistics</span></h2>
    <div class="stats-divider"></div>
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-icon-container">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00FF41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                    <polyline points="22 4 12 14.01 9 11.01"/>
                </svg>
            </div>
            <div class="stat-number">5+</div>
            <div class="stat-label">Completed Projects</div>
        </div>
        <div class="stat-item">
            <div class="stat-icon-container stat-icon-orange">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                    <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
                </svg>
            </div>
            <div class="stat-number stat-number-orange">3+</div>
            <div class="stat-label">Achievements</div>
        </div>
        <div class="stat-item">
            <div class="stat-icon-container stat-icon-blue">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4A9EFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
            </div>
            <div class="stat-number stat-number-blue">100%</div>
            <div class="stat-label">Passion</div>
        </div>
        <div class="stat-item">
            <div class="stat-icon-container stat-icon-purple">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#DDA0DD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                </svg>
            </div>
            <div class="stat-number stat-number-purple">24/7</div>
            <div class="stat-label">Learning</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <h3 class="footer-name">ROBERT MACATIAG</h3>
        <p class="footer-tagline">$ echo "building the future, one project at a time"</p>
        <div class="footer-divider"></div>
        <p class="footer-copyright">
            BUILT WITH <span class="footer-heart">⚡</span>
            BY ROBERT MACATIAG &copy; 2026
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

render_sidebar()