import streamlit as st

def apply_sidebar_styles():
    st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Black+Ops+One&display=swap');

/* ─── Custom Scrollbar ───────────────────────────────── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #030703; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #1A3A1A, #0D1F0D);
    border-radius: 0;
}
::-webkit-scrollbar-thumb:hover { background: #00FF41; }

/* ─── Sidebar Container ──────────────────────────────── */
[data-testid="stSidebar"] {
    min-width: 300px !important;
    max-width: 340px !important;
    background:
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 30px,
            rgba(0, 255, 65, 0.018) 30px,
            rgba(0, 255, 65, 0.018) 31px
        ),
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 30px,
            rgba(0, 255, 65, 0.018) 30px,
            rgba(0, 255, 65, 0.018) 31px
        ),
        linear-gradient(180deg, #050A05 0%, #070D0A 50%, #030703 100%) !important;
    border-right: 1px solid #1A3A1A !important;
    position: relative;
    overflow: hidden;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 1rem !important;
}

/* Scanline overlay on sidebar */
[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.025) 0px,
        rgba(0, 0, 0, 0.025) 1px,
        transparent 1px,
        transparent 3px
    );
    pointer-events: none;
    z-index: 0;
}

/* Green accent line on top of sidebar */
[data-testid="stSidebar"]::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #00FF41, #FF6B00, #00FF41);
    background-size: 200% auto;
    animation: shimmer 4s linear infinite;
    z-index: 10;
}

@keyframes shimmer {
    0%   { background-position: 0% center; }
    100% { background-position: 200% center; }
}

/* ─── Sidebar Typography ─────────────────────────────── */
[data-testid="stSidebar"] .stRadio label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 0.5rem 0 !important;
    color: #4A7A4A !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    transition: color 0.3s ease !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    color: #00FF41 !important;
}

[data-testid="stSidebar"] .stRadio > div { gap: 0.4rem !important; }

[data-testid="stSidebar"] a {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    color: #00FF41 !important;
    text-decoration: none !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    font-family: 'JetBrains Mono', monospace !important;
    color: #4A7A4A !important;
}

[data-testid="stSidebar"] hr {
    border: none !important;
    border-top: 1px solid #1A3A1A !important;
    margin: 1.2rem 0 !important;
}

/* ─── Navigation Links ───────────────────────────────── */
[data-testid="stSidebarNav"] {
    padding-top: 0.5rem !important;
}

[data-testid="stSidebarNav"] a {
    display: flex !important;
    align-items: center !important;
    padding: 0.6rem 1rem !important;
    margin-bottom: 0.3rem !important;
    background: transparent !important;
    border: 1px solid transparent !important;
    border-left: 2px solid transparent !important;
    color: #2A5A2A !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
    clip-path: polygon(
        0 0,
        calc(100% - 8px) 0,
        100% 8px,
        100% 100%,
        8px 100%,
        0 calc(100% - 8px)
    ) !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(0, 255, 65, 0.05) !important;
    border-color: #1E3D1E !important;
    border-left-color: #00FF41 !important;
    color: #00FF41 !important;
    transform: translateX(4px) !important;
    box-shadow: 0 0 12px rgba(0,255,65,0.08) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(0, 255, 65, 0.06) !important;
    border-color: #1E3D1E !important;
    border-left-color: #FF6B00 !important;
    color: #00FF41 !important;
    box-shadow: 0 0 16px rgba(0,255,65,0.1) !important;
}

/* ─── Streamlit Components Override ──────────────────── */
.stButton > button {
    background: transparent !important;
    color: #2A5A2A !important;
    border: 1px solid #1E3D1E !important;
    border-radius: 0 !important;
    clip-path: polygon(
        6px 0%, 100% 0%,
        calc(100% - 6px) 100%, 0% 100%
    ) !important;
    padding: 0.5rem 1.2rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: rgba(0,255,65,0.06) !important;
    color: #00FF41 !important;
    border-color: #00FF41 !important;
    box-shadow: 0 0 14px rgba(0,255,65,0.15) !important;
    transform: translateY(-2px) !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    background: rgba(5,10,5,0.8) !important;
    border: 1px solid #1A3A1A !important;
    border-radius: 0 !important;
    color: #C8D8C8 !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00FF41 !important;
    box-shadow: 0 0 0 1px rgba(0,255,65,0.2) !important;
}

/* ─── Tactical Background Animation ──────────────────── */
.tactical-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: -1;
    overflow: hidden;
}

.data-stream {
    position: absolute;
    width: 1px;
    background: linear-gradient(
        180deg,
        transparent,
        rgba(0, 255, 65, 0.12),
        transparent
    );
    animation: stream-fall 8s linear infinite;
}

@keyframes stream-fall {
    0%   { transform: translateY(-100%); opacity: 0; }
    10%  { opacity: 1; }
    90%  { opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

/* ─── Status indicator dot ───────────────────────────── */
@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 4px #00FF41; opacity: 1; }
    50%       { box-shadow: 0 0 14px #00FF41, 0 0 28px rgba(0,255,65,0.4); opacity: 0.8; }
}

/* ─── Mobile Responsive ──────────────────────────────── */
@media screen and (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 270px !important;
        max-width: 300px !important;
    }
}

@media screen and (max-width: 480px) {
    [data-testid="stSidebar"] {
        min-width: 250px !important;
        max-width: 270px !important;
    }
}
</style>

<div class="tactical-bg">
    <span class="data-stream"
          style="left:12%; animation-delay:0s; height:160px;"></span>
    <span class="data-stream"
          style="left:32%; animation-delay:2.5s; height:220px;"></span>
    <span class="data-stream"
          style="left:58%; animation-delay:4.2s; height:180px;"></span>
    <span class="data-stream"
          style="left:78%; animation-delay:6.5s; height:140px;"></span>
    <span class="data-stream"
          style="left:92%; animation-delay:1.8s; height:200px;"></span>
</div>
''', unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:

        # ── Profile Block ─────────────────────────────────────
        profile_html = '''
<div style="
    text-align: left;
    margin-bottom: 1.8rem;
    padding: 0 0.5rem;
    position: relative;
    z-index: 1;
">
    <!-- Status bar -->
    <div style="
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 1.2rem;
        font-family: JetBrains Mono, monospace;
        font-size: 0.65rem;
        color: #2A4A2A;
        letter-spacing: 2px;
        text-transform: uppercase;
    ">
        <div style="
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #00FF41;
            animation: pulse-dot 2s ease-in-out infinite;
        "></div>
        <span style="color:#00FF41;">ONLINE</span>
        <span style="color:#1A3A1A;">|</span>
        <span style="color:#FF6B00;">SYS_ACTIVE</span>
    </div>

    <!-- Tactical Avatar Frame -->
    <div style="
        width: 72px; height: 72px;
        background: rgba(5,10,5,0.9);
        border: 1px solid #1A3A1A;
        margin: 0 auto 1.4rem 0;
        display: flex;
        align-items: center;
        justify-content: center;
        clip-path: polygon(
            0 10px, 10px 0,
            calc(100% - 10px) 0, 100% 10px,
            100% calc(100% - 10px), calc(100% - 10px) 100%,
            10px 100%, 0 calc(100% - 10px)
        );
        position: relative;
        box-shadow: 0 0 20px rgba(0,255,65,0.08);
    ">
        <!-- TL corner -->
        <div style="
            position:absolute; top:-1px; left:-1px;
            width:14px; height:14px;
            border-top:2px solid #00FF41;
            border-left:2px solid #00FF41;
        "></div>
        <!-- BR corner -->
        <div style="
            position:absolute; bottom:-1px; right:-1px;
            width:14px; height:14px;
            border-bottom:2px solid #FF6B00;
            border-right:2px solid #FF6B00;
        "></div>
        <span style="
            font-size: 2rem;
            filter: drop-shadow(0 0 6px rgba(0,255,65,0.5));
        ">⌨️</span>
    </div>

    <!-- Operator prompt -->
    <div style="margin-bottom: 0.3rem;">
        <span style="
            color: #FF6B00;
            font-family: JetBrains Mono, monospace;
            font-size: 0.7rem;
            letter-spacing: 1px;
        ">$ operator --id</span>
    </div>

    <!-- Name -->
    <h2 style="
        color: #E8F5E9;
        font-family: Black Ops One, cursive;
        margin: 0 0 0.4rem 0;
        font-size: 1.4rem;
        font-weight: 400;
        letter-spacing: 3px;
        text-transform: uppercase;
        text-shadow:
            0 0 20px rgba(0,255,65,0.15),
            1px 1px 0px #0A1A0A;
        line-height: 1.1;
    ">Robert<br>Macatiag</h2>

    <!-- Role tag -->
    <div style="
        display: inline-flex;
        align-items: center;
        background: rgba(255,107,0,0.06);
        border: 1px solid rgba(255,107,0,0.25);
        border-left: 3px solid #FF6B00;
        padding: 0.35rem 0.8rem;
        margin-top: 0.4rem;
        clip-path: polygon(
            0 0,
            calc(100% - 8px) 0,
            100% 50%,
            calc(100% - 8px) 100%,
            0 100%
        );
    ">
        <span style="
            font-family: JetBrains Mono, monospace;
            font-size: 0.68rem;
            color: #FF8C00;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
        ">CS_STUDENT / DEV</span>
    </div>
</div>
'''
        st.html(profile_html)

        # ── Divider ───────────────────────────────────────────
        st.markdown('''
<div style="
    height: 1px;
    background: linear-gradient(90deg, #1A3A1A, #2A5A2A, #1A3A1A);
    margin: 0 0 1.4rem 0;
    position: relative;
    z-index: 1;
">
    <div style="
        position: absolute;
        left: 50%; top: -4px;
        transform: translateX(-50%);
        width: 8px; height: 8px;
        background: #00FF41;
        clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        box-shadow: 0 0 6px #00FF41;
    "></div>
</div>
''', unsafe_allow_html=True)

        # ── Quick Stats ───────────────────────────────────────
        stats_html = '''
<div style="
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.6rem;
    margin-bottom: 1.4rem;
    padding: 0 0.2rem;
    position: relative;
    z-index: 1;
">
    <div style="
        background: rgba(0,0,0,0.35);
        border: 1px solid #1A3A1A;
        border-top: 2px solid #00FF41;
        padding: 0.8rem 0.7rem;
        text-align: center;
        clip-path: polygon(
            0 0,
            calc(100% - 8px) 0,
            100% 8px,
            100% 100%,
            8px 100%,
            0 calc(100% - 8px)
        );
    ">
        <div style="
            font-family: Black Ops One, cursive;
            font-size: 1.3rem;
            color: #00FF41;
            letter-spacing: 1px;
            text-shadow: 0 0 12px rgba(0,255,65,0.3);
        ">3rd</div>
        <div style="
            font-family: JetBrains Mono, monospace;
            font-size: 0.6rem;
            color: #2A5A2A;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-top: 0.15rem;
        ">Year</div>
    </div>
    <div style="
        background: rgba(0,0,0,0.35);
        border: 1px solid #1A3A1A;
        border-top: 2px solid #FF6B00;
        padding: 0.8rem 0.7rem;
        text-align: center;
        clip-path: polygon(
            0 0,
            calc(100% - 8px) 0,
            100% 8px,
            100% 100%,
            8px 100%,
            0 calc(100% - 8px)
        );
    ">
        <div style="
            font-family: Black Ops One, cursive;
            font-size: 1.3rem;
            color: #FF6B00;
            letter-spacing: 1px;
            text-shadow: 0 0 12px rgba(255,107,0,0.3);
        ">3+</div>
        <div style="
            font-family: JetBrains Mono, monospace;
            font-size: 0.6rem;
            color: #2A5A2A;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-top: 0.15rem;
        ">Projects</div>
    </div>
    <div style="
        background: rgba(0,0,0,0.35);
        border: 1px solid #1A3A1A;
        border-top: 2px solid #4A9EFF;
        padding: 0.8rem 0.7rem;
        text-align: center;
        clip-path: polygon(
            0 0,
            calc(100% - 8px) 0,
            100% 8px,
            100% 100%,
            8px 100%,
            0 calc(100% - 8px)
        );
    ">
        <div style="
            font-family: Black Ops One, cursive;
            font-size: 1.3rem;
            color: #4A9EFF;
            letter-spacing: 1px;
            text-shadow: 0 0 12px rgba(74,158,255,0.3);
        ">2+</div>
        <div style="
            font-family: JetBrains Mono, monospace;
            font-size: 0.6rem;
            color: #2A5A2A;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-top: 0.15rem;
        ">Certs</div>
    </div>
    <div style="
        background: rgba(0,0,0,0.35);
        border: 1px solid #1A3A1A;
        border-top: 2px solid #DDA0DD;
        padding: 0.8rem 0.7rem;
        text-align: center;
        clip-path: polygon(
            0 0,
            calc(100% - 8px) 0,
            100% 8px,
            100% 100%,
            8px 100%,
            0 calc(100% - 8px)
        );
    ">
        <div style="
            font-family: Black Ops One, cursive;
            font-size: 1.3rem;
            color: #DDA0DD;
            letter-spacing: 1px;
            text-shadow: 0 0 12px rgba(221,160,221,0.3);
        ">3+</div>
        <div style="
            font-family: JetBrains Mono, monospace;
            font-size: 0.6rem;
            color: #2A5A2A;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-top: 0.15rem;
        ">Awards</div>
    </div>
</div>
'''
        st.html(stats_html)

        # ── Divider ───────────────────────────────────────────
        st.markdown('''
<div style="
    height: 1px;
    background: linear-gradient(90deg, #1A3A1A, #2A5A2A, #1A3A1A);
    margin: 0 0 1.4rem 0;
    position: relative; z-index: 1;
"></div>
''', unsafe_allow_html=True)

        # ── Connect Block ─────────────────────────────────────
        connect_html = '''
<div style="
    padding: 1.2rem 1rem;
    background: rgba(5,10,5,0.5);
    border: 1px solid #1A3A1A;
    border-left: 3px solid #2A4A2A;
    position: relative;
    z-index: 1;
    clip-path: polygon(
        0 0,
        calc(100% - 10px) 0,
        100% 10px,
        100% 100%,
        10px 100%,
        0 calc(100% - 10px)
    );
    margin-bottom: 1.4rem;
">
    <!-- Corner accent -->
    <div style="
        position:absolute; top:0; right:0;
        width:10px; height:10px;
        background:#1A3A1A;
        clip-path: polygon(0 0, 100% 0, 100% 100%);
    "></div>

    <p style="
        color: #2A5A2A;
        font-size: 0.68rem;
        margin-bottom: 1rem;
        font-weight: 600;
        font-family: JetBrains Mono, monospace;
        letter-spacing: 2px;
        text-transform: uppercase;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    ">
        <span style="color:#FF6B00;">//</span> CONNECT
    </p>

    <div style="display: flex; gap: 0.6rem; flex-wrap: wrap;">

        <!-- GitHub -->
        <a href="https://github.com" target="_blank" style="
            width: 40px; height: 40px;
            background: rgba(0,0,0,0.5);
            border: 1px solid #1E3D1E;
            display: flex; align-items: center; justify-content: center;
            text-decoration: none;
            clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
            transition: all 0.3s ease;
        "
        onmouseover="
            this.style.borderColor='#00FF41';
            this.style.boxShadow='0 0 12px rgba(0,255,65,0.2)';
            this.style.background='rgba(0,255,65,0.05)';
            this.querySelector('svg').style.stroke='#00FF41';
        "
        onmouseout="
            this.style.borderColor='#1E3D1E';
            this.style.boxShadow='none';
            this.style.background='rgba(0,0,0,0.5)';
            this.querySelector('svg').style.stroke='#2A5A2A';
        ">
            <svg width="18" height="18" viewBox="0 0 24 24"
                 fill="none" stroke="#2A5A2A" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round"
                 style="transition: stroke 0.3s ease;">
                <path d="M9 19c-5 1.5-5-2.5-7-3
                         m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61
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
        </a>

        <!-- LinkedIn -->
        <a href="https://linkedin.com" target="_blank" style="
            width: 40px; height: 40px;
            background: rgba(0,0,0,0.5);
            border: 1px solid #1E3D1E;
            display: flex; align-items: center; justify-content: center;
            text-decoration: none;
            clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
            transition: all 0.3s ease;
        "
        onmouseover="
            this.style.borderColor='#00FF41';
            this.style.boxShadow='0 0 12px rgba(0,255,65,0.2)';
            this.style.background='rgba(0,255,65,0.05)';
            this.querySelector('svg').style.stroke='#00FF41';
        "
        onmouseout="
            this.style.borderColor='#1E3D1E';
            this.style.boxShadow='none';
            this.style.background='rgba(0,0,0,0.5)';
            this.querySelector('svg').style.stroke='#2A5A2A';
        ">
            <svg width="18" height="18" viewBox="0 0 24 24"
                 fill="none" stroke="#2A5A2A" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round"
                 style="transition: stroke 0.3s ease;">
                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7
                         a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7
                         a6 6 0 0 1 6-6z"/>
                <rect x="2" y="9" width="4" height="12"/>
                <circle cx="4" cy="4" r="2"/>
            </svg>
        </a>

        <!-- Facebook -->
        <a href="https://facebook.com" target="_blank" style="
            width: 40px; height: 40px;
            background: rgba(0,0,0,0.5);
            border: 1px solid #1E3D1E;
            display: flex; align-items: center; justify-content: center;
            text-decoration: none;
            clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
            transition: all 0.3s ease;
        "
        onmouseover="
            this.style.borderColor='#00FF41';
            this.style.boxShadow='0 0 12px rgba(0,255,65,0.2)';
            this.style.background='rgba(0,255,65,0.05)';
            this.querySelector('svg').style.stroke='#00FF41';
        "
        onmouseout="
            this.style.borderColor='#1E3D1E';
            this.style.boxShadow='none';
            this.style.background='rgba(0,0,0,0.5)';
            this.querySelector('svg').style.stroke='#2A5A2A';
        ">
            <svg width="18" height="18" viewBox="0 0 24 24"
                 fill="none" stroke="#2A5A2A" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round"
                 style="transition: stroke 0.3s ease;">
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
            </svg>
        </a>

        <!-- Email -->
        <a href="mailto:robertmacatiag@email.com" style="
            width: 40px; height: 40px;
            background: rgba(0,0,0,0.5);
            border: 1px solid #1E3D1E;
            display: flex; align-items: center; justify-content: center;
            text-decoration: none;
            clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
            transition: all 0.3s ease;
        "
        onmouseover="
            this.style.borderColor='#FF6B00';
            this.style.boxShadow='0 0 12px rgba(255,107,0,0.2)';
            this.style.background='rgba(255,107,0,0.05)';
            this.querySelector('svg').style.stroke='#FF6B00';
        "
        onmouseout="
            this.style.borderColor='#1E3D1E';
            this.style.boxShadow='none';
            this.style.background='rgba(0,0,0,0.5)';
            this.querySelector('svg').style.stroke='#2A5A2A';
        ">
            <svg width="18" height="18" viewBox="0 0 24 24"
                 fill="none" stroke="#2A5A2A" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round"
                 style="transition: stroke 0.3s ease;">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2
                         H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
            </svg>
        </a>

    </div>
</div>
'''
        st.html(connect_html)

        # ── System Info Block ──────────────────────────────────
        sysinfo_html = '''
<div style="
    padding: 1rem;
    border: 1px solid #0F1F0F;
    background: rgba(0,0,0,0.25);
    position: relative;
    z-index: 1;
    margin-bottom: 0.5rem;
">
    <p style="
        font-family: JetBrains Mono, monospace;
        font-size: 0.6rem;
        color: #1A3A1A;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin: 0 0 0.5rem 0;
    ">// SYS_INFO</p>
    <p style="
        font-family: JetBrains Mono, monospace;
        font-size: 0.65rem;
        color: #1E3D1E;
        margin: 0.2rem 0;
        letter-spacing: 0.5px;
    ">
        <span style="color:#FF6B00;">VER:</span> PORTFOLIO_v2.0
    </p>
    <p style="
        font-family: JetBrains Mono, monospace;
        font-size: 0.65rem;
        color: #1E3D1E;
        margin: 0.2rem 0;
        letter-spacing: 0.5px;
    ">
        <span style="color:#FF6B00;">LANG:</span> Python / Streamlit
    </p>
    <p style="
        font-family: JetBrains Mono, monospace;
        font-size: 0.65rem;
        color: #1E3D1E;
        margin: 0.2rem 0;
        letter-spacing: 0.5px;
    ">
        <span style="color:#FF6B00;">BUILD:</span> 2026
    </p>
    <p style="
        font-family: JetBrains Mono, monospace;
        font-size: 0.65rem;
        color: #00FF41;
        margin: 0.4rem 0 0 0;
        letter-spacing: 0.5px;
        opacity: 0.6;
    ">▌ READY</p>
</div>
'''
        st.html(sysinfo_html)