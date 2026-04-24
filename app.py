import streamlit as st
import streamlit.components.v1 as components
import datetime
import time

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="Develop your arbitration skills With Gesner",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== INITIALIZE SESSION STATE ==========
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "language" not in st.session_state:
    st.session_state.language = "en"
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = 1

# ========== UI TRANSLATIONS ==========
lang_ui = {
    "en": {
        "app_title": "⚖️ Develop your arbitration skills With Gesner",
        "subtitle": "Executive Course – 20 lessons, guest practitioners, and interactive learning",
        "login_header": "Login to access the course",
        "username": "👤 Username",
        "password": "🔒 Password",
        "sign_in": "🚀 Sign In",
        "demo_note": "✨ Demo credentials: any username / any password",
        "welcome": "Welcome",
        "logout": "🚪 Logout",
        "language": "🌐 Language",
        "english": "English",
        "french": "Français",
        "spanish": "Español",
        "price_title": "💰 Pricing",
        "price_one_time": "**One‑time license:** **$299 USD**  \n*Full course access, lifetime updates*",
        "price_monthly": "**Monthly subscription:** **$29 USD / month**  \n*All lessons + audio support*",
        "copyright": "© 2026 GlobalInternet.py – built by Gesner Deslandes",
        "contact": "📞 Contact: (509) 4738-5663 | ✉️ deslandes78@gmail.com",
        "lesson_label": "📖 Lesson",
        "examples": "📝 Key points",
        "summary": "📌 Summary",
        "audio_lesson": "🔊 Listen to lesson",
        "audio_points": "🔊 Listen to key points",
        "next_lesson": "➡️ Next Lesson",
        "prev_lesson": "⬅️ Previous Lesson",
    },
    "fr": {
        "app_title": "⚖️ Développez vos compétences en arbitrage avec Gesner",
        "subtitle": "Cours exécutif – 20 leçons, intervenants invités, apprentissage interactif",
        "login_header": "Connectez-vous pour accéder au cours",
        "username": "👤 Nom d'utilisateur",
        "password": "🔒 Mot de passe",
        "sign_in": "🚀 Se connecter",
        "demo_note": "✨ Identifiants de démonstration : n'importe quel nom/mot de passe",
        "welcome": "Bienvenue",
        "logout": "🚪 Déconnexion",
        "language": "🌐 Langue",
        "english": "Anglais",
        "french": "Français",
        "spanish": "Espagnol",
        "price_title": "💰 Tarifs",
        "price_one_time": "**Licence unique :** **299 $ USD**  \n*Accès complet au cours, mises à jour à vie*",
        "price_monthly": "**Abonnement mensuel :** **29 $ USD / mois**  \n*Toutes les leçons + audio*",
        "copyright": "© 2026 GlobalInternet.py – construit par Gesner Deslandes",
        "contact": "📞 Contact : (509) 4738-5663 | ✉️ deslandes78@gmail.com",
        "lesson_label": "📖 Leçon",
        "examples": "📝 Points clés",
        "summary": "📌 Résumé",
        "audio_lesson": "🔊 Écouter la leçon",
        "audio_points": "🔊 Écouter les points clés",
        "next_lesson": "➡️ Leçon suivante",
        "prev_lesson": "⬅️ Leçon précédente",
    },
    "es": {
        "app_title": "⚖️ Desarrolle sus habilidades de arbitraje con Gesner",
        "subtitle": "Curso ejecutivo – 20 lecciones, profesionales invitados, aprendizaje interactivo",
        "login_header": "Inicie sesión para acceder al curso",
        "username": "👤 Usuario",
        "password": "🔒 Contraseña",
        "sign_in": "🚀 Iniciar sesión",
        "demo_note": "✨ Credenciales de demostración: cualquier usuario/contraseña",
        "welcome": "Bienvenido",
        "logout": "🚪 Cerrar sesión",
        "language": "🌐 Idioma",
        "english": "Inglés",
        "french": "Francés",
        "spanish": "Español",
        "price_title": "💰 Precios",
        "price_one_time": "**Licencia única:** **$299 USD**  \n*Acceso completo al curso, actualizaciones de por vida*",
        "price_monthly": "**Suscripción mensual:** **$29 USD / mes**  \n*Todas las lecciones + audio*",
        "copyright": "© 2026 GlobalInternet.py – construido por Gesner Deslandes",
        "contact": "📞 Contacto: (509) 4738-5663 | ✉️ deslandes78@gmail.com",
        "lesson_label": "📖 Lección",
        "examples": "📝 Puntos clave",
        "summary": "📌 Resumen",
        "audio_lesson": "🔊 Escuchar lección",
        "audio_points": "🔊 Escuchar puntos clave",
        "next_lesson": "➡️ Siguiente lección",
        "prev_lesson": "⬅️ Lección anterior",
    }
}

# ========== 20 UNIQUE LESSONS (ENGLISH) ==========
lessons = [
    {  # Lesson 1
        "title": "Introduction to International Arbitration",
        "explanation": "International arbitration is a private, binding dispute resolution method where parties agree to submit their disputes to one or more arbitrators instead of going to court. It is governed by treaties, national laws, and institutional rules (e.g., ICC, LCIA, SIAC).",
        "key_points": [
            "Consent is the cornerstone: arbitration agreement.",
            "Arbitrators are chosen by the parties.",
            "Award is final and enforceable under the New York Convention.",
        ],
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400&h=250&fit=crop",
        "summary": "You learned the definition of international arbitration, its advantages, and the legal framework that supports it."
    },
    {  # Lesson 2
        "title": "The Arbitration Agreement",
        "explanation": "The arbitration agreement is a written clause or separate contract where parties agree to arbitrate future or existing disputes. It must be valid, clear, and cover the subject matter.",
        "key_points": [
            "Separability doctrine: arbitration clause survives contract termination.",
            "Competence‑competence: tribunal rules on its own jurisdiction.",
            "Form requirements: in writing (electronic accepted).",
        ],
        "image": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=400&h=250&fit=crop",
        "summary": "You now understand the key elements of a valid arbitration agreement and the doctrines that give it effect."
    },
    {  # Lesson 3
        "title": "Institutional vs. Ad Hoc Arbitration",
        "explanation": "Institutional arbitration is administered by a permanent body (ICC, LCIA, SIAC, etc.) with its own rules. Ad hoc arbitration is managed by the parties without an administering institution.",
        "key_points": [
            "Institutional: built‑in administration, scrutiny of awards.",
            "Ad hoc: more flexibility, lower costs, but requires party cooperation.",
            "UNCITRAL Rules often used for ad hoc.",
        ],
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=400&h=250&fit=crop",
        "summary": "You can now choose between institutional and ad hoc arbitration based on the needs of the dispute."
    },
    {  # Lesson 4
        "title": "Selecting Arbitrators",
        "explanation": "Parties may select arbitrators based on expertise, availability, and impartiality. Typically, each party appoints one arbitrator, and the two appoint the presiding arbitrator.",
        "key_points": [
            "Criteria: legal background, industry knowledge, language, nationality.",
            "Challenge procedure for lack of impartiality.",
            "Institutional rules provide default appointment mechanisms.",
        ],
        "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=400&h=250&fit=crop",
        "summary": "You learned how arbitrators are chosen and the importance of a balanced, competent tribunal."
    },
    {  # Lesson 5
        "title": "Commencing Arbitration",
        "explanation": "Commencement starts with a request for arbitration (Notice of Arbitration) sent to the other party and/or the institution. It must describe the dispute, the relief sought, and the proposed arbitrators.",
        "key_points": [
            "Notice triggers time limits and appointment deadlines.",
            "Answer or response from respondent follows.",
            "Seat of arbitration should be designated.",
        ],
        "image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400&h=250&fit=crop",
        "summary": "You understand the procedural steps to formally start an arbitration case."
    },
    {  # Lesson 6
        "title": "Jurisdiction of the Arbitral Tribunal",
        "explanation": "The tribunal has the power to rule on its own jurisdiction (competence‑competence). It may decide whether the arbitration agreement is valid, the dispute falls within its scope, or whether conditions are met.",
        "key_points": [
            "Objections to jurisdiction must be raised early.",
            "Separability doctrine applies.",
            "Tribunal's decision can be reviewed by state courts.",
        ],
        "image": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400&h=250&fit=crop",
        "summary": "You now know how arbitral tribunals determine their own authority and the limited court review."
    },
    {  # Lesson 7
        "title": "Procedural Orders and Timetables",
        "explanation": "After constitution, the tribunal issues procedural orders setting the schedule for submissions, evidence, and hearings. A typical timetable includes pleadings, document production, witness statements, and a hearing.",
        "key_points": [
            "Procedural order No. 1 often addresses language, place, and rules.",
            "Redfern Schedule for document production.",
            "Flexibility tailored to complexity.",
        ],
        "image": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=400&h=250&fit=crop",
        "summary": "You learned how the arbitration timetable is established and what it typically contains."
    },
    {  # Lesson 8
        "title": "Document Production",
        "explanation": "Document production is a unique feature of international arbitration, allowing parties to request relevant documents from each other. It is more limited than US‑style discovery.",
        "key_points": [
            "Redfern Schedule format: request, objection, tribunal ruling.",
            "IBA Rules on the Taking of Evidence guide the process.",
            "Proportionality and relevance are key.",
        ],
        "image": "https://images.unsplash.com/photo-1507924538820-ede94a04019d?w=400&h=250&fit=crop",
        "summary": "You understand the document production process and how to manage it effectively."
    },
    {  # Lesson 9
        "title": "Witnesses and Experts",
        "explanation": "Fact witnesses and expert witnesses provide evidence through written statements and oral testimony at the hearing. Experts may be party‑appointed or tribunal‑appointed.",
        "key_points": [
            "Witness statements must be factual and relevant.",
            "Cross‑examination is permitted but controlled.",
            "Tribunal may appoint independent experts.",
        ],
        "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=400&h=250&fit=crop",
        "summary": "You learned how to prepare witnesses and use expert evidence in arbitration."
    },
    {  # Lesson 10
        "title": "The Arbitration Hearing",
        "explanation": "The hearing is where the tribunal hears oral arguments, examines witnesses, and assesses evidence. It typically lasts from one day to several weeks, depending on complexity.",
        "key_points": [
            "Opening statements, examination, closing arguments.",
            "Interpretation and transcription services often used.",
            "Post‑hearing briefs may be submitted.",
        ],
        "image": "https://images.unsplash.com/photo-1521791055366-0d553872125f?w=400&h=250&fit=crop",
        "summary": "You now know what to expect during an arbitration hearing and how to prepare."
    },
    {  # Lesson 11
        "title": "The Arbitral Award",
        "explanation": "The final award resolves all issues submitted to arbitration. It must be in writing, reasoned, signed by arbitrators, and dated. Lack of reasoning may be grounds for annulment.",
        "key_points": [
            "Types: final award, partial award, consent award.",
            "Deliberations and voting process.",
            "Correction and interpretation of awards.",
        ],
        "image": "https://images.unsplash.com/photo-1575505586569-646b2ca898fc?w=400&h=250&fit=crop",
        "summary": "You understand the characteristics of a valid arbitral award and its effects."
    },
    {  # Lesson 12
        "title": "Confidentiality in Arbitration",
        "explanation": "Confidentiality is a perceived advantage, but it is not automatic. Many institutional rules provide for confidentiality of the proceedings, but not necessarily the award.",
        "key_points": [
            "ICC, LCIA rules include confidentiality provisions.",
            "Parties may agree on enhanced confidentiality.",
            "Exceptions: court challenges, enforcement proceedings.",
        ],
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=400&h=250&fit=crop",
        "summary": "You learned the scope and limits of confidentiality in international arbitration."
    },
    {  # Lesson 13
        "title": "Challenging and Enforcing Awards",
        "explanation": "Awards can be challenged at the seat of arbitration (annulment) or resisted during enforcement. The New York Convention provides a uniform framework for recognition and enforcement.",
        "key_points": [
            "Grounds for setting aside: procedural defects, public policy.",
            "Enforcement may be refused on limited grounds (Art. V NYC).",
            "Enforcement is generally easier than court judgments.",
        ],
        "image": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=400&h=250&fit=crop",
        "summary": "You now know how to challenge an award and how to enforce it across borders."
    },
    {  # Lesson 14
        "title": "Interim Measures",
        "explanation": "The tribunal may order interim measures to preserve the status quo, secure assets, or prevent harm. Courts can also issue emergency relief before tribunal constitution.",
        "key_points": [
            "Conditions: urgency, irreparable harm, prima facie case.",
            "Emergency arbitrator provisions in many rules.",
            "Failure to comply may lead to adverse inferences.",
        ],
        "image": "https://images.unsplash.com/photo-1507924538820-ede94a04019d?w=400&h=250&fit=crop",
        "summary": "You learned how to request and obtain interim measures in arbitration."
    },
    {  # Lesson 15
        "title": "Costs and Fee Structures",
        "explanation": "Arbitration costs include arbitrator fees, institutional fees, legal fees, and administrative expenses. The award may allocate costs between parties.",
        "key_points": [
            "Ad valorem vs. hourly fee models.",
            "Deposits on account required.",
            "Costs follow the event in most institutional rules.",
        ],
        "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=400&h=250&fit=crop",
        "summary": "You understand how arbitration costs are calculated and allocated."
    },
    {  # Lesson 16
        "title": "Investment Arbitration (ISDS)",
        "explanation": "Investment arbitration allows foreign investors to sue host States under bilateral investment treaties (BITs). It is governed by ICSID or UNCITRAL rules.",
        "key_points": [
            "Treaty‑based consent, fair and equitable treatment.",
            "ICSID Convention provides self‑contained enforcement.",
            "Recent reforms and criticisms.",
        ],
        "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=400&h=250&fit=crop",
        "summary": "You were introduced to the distinct field of investor‑State dispute settlement."
    },
    {  # Lesson 17
        "title": "Role of National Courts",
        "explanation": "National courts support arbitration by enforcing arbitration agreements, granting interim measures, appointing arbitrators (if needed), and reviewing awards (set‑aside).",
        "key_points": [
            "Anti‑suit injunctions to prevent court proceedings.",
            "Courts may assist in taking evidence.",
            "Limited judicial intervention under Art. 5 UNCITRAL Model Law.",
        ],
        "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=400&h=250&fit=crop",
        "summary": "You learned the supportive and supervisory role of state courts in arbitration."
    },
    {  # Lesson 18
        "title": "Ethical Considerations for Arbitrators",
        "explanation": "Arbitrators must be independent and impartial. Disclosure of any potential conflicts of interest is mandatory under the IBA Guidelines.",
        "key_points": [
            "Red, orange, and green lists for conflicts.",
            "Duty to disclose facts that may give rise to justifiable doubts.",
            "Challenge procedure for lack of impartiality.",
        ],
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=400&h=250&fit=crop",
        "summary": "You understand the ethical standards that arbitrators must follow."
    },
    {  # Lesson 19
        "title": "Practical Tips for Arbitration Advocacy",
        "explanation": "Effective advocacy in arbitration requires adapting to the tribunal's style, brevity, and cultural awareness.",
        "key_points": [
            "Know the arbitrators' background and preferences.",
            "Use visuals and written chronologies.",
            "Be respectful but concise.",
        ],
        "image": "https://images.unsplash.com/photo-1521791055366-0d553872125f?w=400&h=250&fit=crop",
        "summary": "You gained practical tips to present your case persuasively in arbitration."
    },
    {  # Lesson 20
        "title": "Future Trends in International Arbitration",
        "explanation": "Arbitration is evolving with technology (online hearings), greater diversity among arbitrators, and efforts to increase efficiency and transparency.",
        "key_points": [
            "Virtual hearings and AI‑assisted document review.",
            "Gender and geographic diversity initiatives.",
            "Expedited procedures for smaller claims.",
        ],
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400&h=250&fit=crop",
        "summary": "You explored emerging trends that will shape the future of international arbitration."
    }
]

# ========== HELPER FUNCTIONS ==========
def get_ui_text(key):
    return lang_ui[st.session_state.language].get(key, key)

def audio_button(text, key_suffix):
    """Generate an HTML button that reads the text aloud."""
    escaped = text.replace("'", "\\'").replace('"', '\\"')
    html = f"""
    <script>
    function speak_{key_suffix}() {{
        var msg = new SpeechSynthesisUtterance("{escaped}");
        msg.lang = "{st.session_state.language}";
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msg);
    }}
    </script>
    <button onclick="speak_{key_suffix}()" style="background-color:#4CAF50; border:none; border-radius:20px; padding:5px 15px; color:white; cursor:pointer;">
        🔊 {get_ui_text('audio_lesson')}
    </button>
    """
    components.html(html, height=40)
    return

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #f0f4ff 0%, #e8f0fe 100%); }
    .main-header { background: linear-gradient(90deg, #1e3c72, #2a5298, #8e24aa, #ffb74d); padding: 1rem; border-radius: 20px; color: white; text-align: center; margin-bottom: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .lesson-card { background-color: white; border-radius: 20px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-left: 8px solid #ffb74d; }
    .points-box { background-color: #f5f5f5; border-radius: 15px; padding: 1rem; margin: 0.5rem 0; }
    .summary-box { background-color: #fff8e1; border-radius: 15px; padding: 1rem; margin-top: 1rem; }
    .stButton>button { background: linear-gradient(90deg, #1e3c72, #2a5298); color: white; border: none; border-radius: 30px; padding: 0.5rem 1.5rem; font-weight: bold; }
    .sidebar .sidebar-content { background-color: #2c3e50; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ========== LOGIN PAGE ==========
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #1e3c72;">⚖️ {get_ui_text('app_title')}</h1>
            <p style="color: #555;">{get_ui_text('subtitle')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Language selector
        lang_options = {"en": get_ui_text("english"), "es": get_ui_text("spanish"), "fr": get_ui_text("french")}
        selected = st.selectbox(get_ui_text("language"), list(lang_options.keys()), format_func=lambda x: lang_options[x])
        if selected != st.session_state.language:
            st.session_state.language = selected
            st.rerun()
        
        with st.form("login"):
            username = st.text_input(get_ui_text("username"))
            password = st.text_input(get_ui_text("password"), type="password")
            if st.form_submit_button(get_ui_text("sign_in"), use_container_width=True) and username and password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            elif st.form_submit_button:
                st.error("Please enter username and password.")
        
        st.markdown(f"<p style='text-align:center;'>{get_ui_text('demo_note')}</p>", unsafe_allow_html=True)

# ========== MAIN DASHBOARD ==========
def main_app():
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/null/balance-scale.png", width=80)
        st.markdown(f"**{get_ui_text('welcome')}, {st.session_state.username}!**")
        st.markdown("---")
        # Language selector
        lang_options = {"en": get_ui_text("english"), "es": get_ui_text("spanish"), "fr": get_ui_text("french")}
        selected = st.selectbox(get_ui_text("language"), list(lang_options.keys()), format_func=lambda x: lang_options[x], key="sidebar_lang")
        if selected != st.session_state.language:
            st.session_state.language = selected
            st.rerun()
        st.markdown("---")
        st.markdown(f"### {get_ui_text('price_title')}")
        st.markdown(get_ui_text("price_one_time"))
        st.markdown("")
        st.markdown(get_ui_text("price_monthly"))
        st.markdown("---")
        st.markdown(get_ui_text("contact"))
        st.markdown("---")
        if st.button(get_ui_text("logout"), use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
        st.caption(get_ui_text("copyright"))
    
    # Header
    st.markdown(f"""
    <div class="main-header">
        <h1>{get_ui_text('app_title')}</h1>
        <p>{get_ui_text('subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Lesson navigation
    col1, col2, col3 = st.columns([1,4,1])
    with col1:
        if st.button(get_ui_text("prev_lesson")):
            if st.session_state.current_lesson > 1:
                st.session_state.current_lesson -= 1
                st.rerun()
    with col2:
        lesson_num = st.selectbox(get_ui_text("lesson_label"), list(range(1,21)), index=st.session_state.current_lesson-1)
        if lesson_num != st.session_state.current_lesson:
            st.session_state.current_lesson = lesson_num
            st.rerun()
    with col3:
        if st.button(get_ui_text("next_lesson")):
            if st.session_state.current_lesson < 20:
                st.session_state.current_lesson += 1
                st.rerun()
    
    lesson = lessons[st.session_state.current_lesson - 1]
    
    # Two columns: left text, right image
    col_left, col_right = st.columns([2,1])
    with col_left:
        st.markdown(f"## {lesson['title']}")
        st.markdown("#### 📖 Explanation")
        st.write(lesson['explanation'])
        if st.button(get_ui_text("audio_lesson"), key=f"audio_lesson_{st.session_state.current_lesson}"):
            audio_button(lesson['explanation'], f"lesson_{st.session_state.current_lesson}")
        
        st.markdown(f"### {get_ui_text('examples')}")
        for idx, point in enumerate(lesson['key_points']):
            st.markdown(f'<div class="points-box">• {point}</div>', unsafe_allow_html=True)
        if st.button(get_ui_text("audio_points"), key=f"audio_points_{st.session_state.current_lesson}"):
            full_points = " ".join(lesson['key_points'])
            audio_button(full_points, f"points_{st.session_state.current_lesson}")
        
        st.markdown(f'<div class="summary-box"><b>{get_ui_text("summary")}</b><br>{lesson["summary"]}</div>', unsafe_allow_html=True)
    
    with col_right:
        # Display image
        try:
            st.image(lesson['image'], use_container_width=True, caption="Illustrative image")
        except:
            st.image("https://via.placeholder.com/400x250?text=Arbitration+Image", use_container_width=True)
        st.markdown("*Image for illustration only*")
    
    st.markdown("---")
    st.caption("Built with 💖 by Gesner Deslandes | GlobalInternet.py")

# ========== ROUTING ==========
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
