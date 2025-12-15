import streamlit as st

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="Bui Tien Duc | Academic Profile",
    page_icon="🎓",
    layout="wide"
)

# =========================
# Data (based on your README)
# =========================
PROFILE = {
    "name": "Bùi Tiến Đức",
    "headline": "Lecturer in Artificial Intelligence, Machine Learning & Data Science",
    "location": "Ho Chi Minh City, Vietnam",
    "github": "https://github.com/BuiTienDuc",
    # From README section "Hồ sơ học thuật | Academic Badges"
    "scopus": "https://www.scopus.com",   # bạn có thể thay bằng link profile Scopus cụ thể
    "orcid": "https://orcid.org",         # bạn có thể thay bằng ORCID cụ thể
    # Image you gave (use raw=1 for Streamlit)
    "banner_img": "https://github.com/BuiTienDuc/BuiTienDuc/blob/main/BUI%20TIEN%20DUC%20Github.jpg?raw=1",
}

RESEARCH_INTERESTS_VI = [
    "Trí tuệ Nhân tạo",
    "Học máy",
    "Blockchain",
    "NLP",
    "Kho dữ liệu và BI",
    "AI trong giao thông, y tế, giáo dục",
]

RESEARCH_INTERESTS_EN = [
    "Artificial Intelligence",
    "Machine Learning",
    "Blockchain and Smart Contracts",
    "Natural Language Processing",
    "Data Warehousing and Business Intelligence",
    "AI for transportation, healthcare, and education",
]

PUBLICATIONS = [
    {
        "venue": "JMM — Journal of Mobile Multimedia (SCOPUS Q2)",
        "title": "Crowdsourced Camera Data Fusion for Urban Traffic Estimation and Monitoring",
        "doi_or_id": "10.13052/jmm1550-4646.2116",
        "link": "https://journals.riverpublishers.com/index.php/JMM/article/view/27637",
    },
    {
        "venue": "ACM — Blockchain & NFTs (SCOPUS + SCI)",
        "title": "Enhancing Transparency and Traceability in Handicrafts Supply Chains Using Blockchain & NFTs",
        "doi_or_id": "10.1145/3719384.3719450",
        "link": "https://dl.acm.org/doi/10.1145/3719384.3719450",
    },
    {
        "venue": "Springer — Intelligence of Things (SCOPUS)",
        "title": "Towards an Approach of Traffic Information Extraction Through ChatGPT",
        "doi_or_id": "ISBN 978-3-031-75596-5",
        "link": "https://link.springer.com/book/10.1007/978-3-031-75596-5",
    },
    {
        "venue": "IEEE ICDABI (SCOPUS)",
        "title": "Designing a Data Warehouse Framework for Business Intelligence",
        "doi_or_id": "10.1109/ICDABI56818.2022.10041706",
        "link": "https://doi.org/10.1109/ICDABI56818.2022.10041706",
    },
]

# GitHub stats (images)
GITHUB_USERNAME = "BuiTienDuc"
STATS_1 = f"https://github-readme-stats.vercel.app/api?username={GITHUB_USERNAME}&show_icons=true"
STATS_2 = f"https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB_USERNAME}&layout=compact"

# =========================
# Sidebar navigation
# =========================
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Me",
        "Teaching Philosophy",
        "Research Interests",
        "Teaching Profile",
        "Research Supervision",
        "National Research Projects",
        "Publications (Selected)",
        "Project Highlights",
        "GitHub Stats",
        "Contact",
    ],
    index=0
)

# =========================
# Header / Home
# =========================
if section == "Home":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.title(PROFILE["name"])
        st.subheader(PROFILE["headline"])
        st.write(f"📍 {PROFILE['location']}")
        st.markdown(
            f"""
            **Academic Badges / Hồ sơ học thuật**  
            - Scopus: {PROFILE['scopus']}
            - ORCID: {PROFILE['orcid']}
            """
        )
        st.markdown("---")
        st.markdown("### Mục lục | Table of Contents")
        st.markdown(
            """
            - ABOUT ME
            - TEACHING PHILOSOPHY
            - RESEARCH INTERESTS
            - TEACHING PROFILE
            - RESEARCH SUPERVISION
            - NATIONAL RESEARCH PROJECTS
            - PUBLICATIONS (SELECTED)
            - PROJECT HIGHLIGHTS
            - GITHUB STATS
            - CONTACT
            """
        )
    with col2:
        st.image(PROFILE["banner_img"], use_container_width=True)

# =========================
# About Me
# =========================
elif section == "About Me":
    st.header("1. ABOUT ME - GIỚI THIỆU")
    tab_vi, tab_en = st.tabs(["VN", "EN"])
    with tab_vi:
        st.write(
            "Xin chào, tôi là Bùi Tiến Đức, Giảng viên Đại học và Nhà nghiên cứu trong các lĩnh vực "
            "Trí tuệ Nhân tạo, Blockchain, Học máy, NLP và Hệ thống thông tin. "
            "Tôi tham gia giảng dạy và hướng dẫn sinh viên công bố các bài báo thuộc hệ SCOPUS và SCI."
        )
    with tab_en:
        st.write(
            "I am Bui Tien Duc, a lecturer and academic researcher specializing in Artificial Intelligence, "
            "Machine Learning, NLP, Blockchain, and Information Systems. "
            "I actively teach, conduct research, and supervise students toward SCOPUS/SCI publications."
        )

# =========================
# Teaching Philosophy
# =========================
elif section == "Teaching Philosophy":
    st.header("2. TEACHING PHILOSOPHY - TRIẾT LÝ GIẢNG DẠY")
    tab_vi, tab_en = st.tabs(["VN", "EN"])
    with tab_vi:
        st.write("Tôi tin rằng giáo dục hiệu quả nuôi dưỡng tư duy phản biện, động lực nghiên cứu và năng lực giải quyết vấn đề thực tiễn.")
    with tab_en:
        st.write("I believe effective education fosters critical thinking, research motivation, and real world problem solving abilities.")

# =========================
# Research Interests
# =========================
elif section == "Research Interests":
    st.header("3. RESEARCH INTERESTS - LĨNH VỰC NGHIÊN CỨU")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("VN")
        for x in RESEARCH_INTERESTS_VI:
            st.markdown(f"- {x}")
    with col2:
        st.subheader("EN")
        for x in RESEARCH_INTERESTS_EN:
            st.markdown(f"- {x}")

# =========================
# Teaching Profile
# =========================
elif section == "Teaching Profile":
    st.header("4. TEACHING PROFILE - HỒ SƠ GIẢNG DẠY")
    st.markdown(
        """
        **VN**
        - ĐH Bách Khoa TP.HCM – Giảng viên thỉnh giảng  
        - ĐH Nguyễn Tất Thành – Giảng viên cơ hữu (2021–2025)

        **EN**
        - HCMUT – Visiting Lecturer  
        - NTTU – Lecturer (2021–2025)
        """
    )

# =========================
# Research Supervision
# =========================
elif section == "Research Supervision":
    st.header("5. RESEARCH SUPERVISION - HƯỚNG DẪN NGHIÊN CỨU")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("VN")
        st.markdown("- ✔ Hướng dẫn sinh viên công bố bài báo SCOPUS/SCI")
        st.markdown("- ✔ Định hướng đề tài AI, Blockchain và NLP")
    with col2:
        st.subheader("EN")
        st.markdown("- ✔ Supervising students for SCOPUS/SCI publications")
        st.markdown("- ✔ Guiding AI, Blockchain, NLP research topics")

# =========================
# National Research Projects
# =========================
elif section == "National Research Projects":
    st.header("6. NATIONAL RESEARCH PROJECTS - ĐỀ TÀI QUỐC GIA")
    st.markdown(
        """
        **VN**
        - Đề tài Quốc gia loại A: AI cho giao thông thông minh  
        - Đề tài Quốc gia loại B: AI chẩn đoán bệnh  

        **EN**
        - National Project Type A: AI for Intelligent Transportation  
        - National Project Type B: AI for Low Back Pain Diagnosis  
        """
    )

# =========================
# Publications
# =========================
elif section == "Publications (Selected)":
    st.header("7. SELECTED PUBLICATIONS - CÔNG BỐ KHOA HỌC (TIÊU BIỂU)")
    for p in PUBLICATIONS:
        with st.expander(f"{p['venue']}"):
            st.markdown(f"**{p['title']}**")
            st.markdown(f"- ID/DOI/ISBN: `{p['doi_or_id']}`")
            st.markdown(f"- Link: {p['link']}")

# =========================
# Project Highlights (placeholder)
# =========================
elif section == "Project Highlights":
    st.header("PROJECT HIGHLIGHTS")
    st.info("Mục này bạn có thể liệt kê các project nổi bật (tên, mô tả ngắn, tech stack, link demo/repo).")

# =========================
# GitHub Stats
# =========================
elif section == "GitHub Stats":
    st.header("GITHUB STATS")
    c1, c2 = st.columns(2)
    with c1:
        st.image(STATS_1, use_container_width=True)
    with c2:
        st.image(STATS_2, use_container_width=True)

# =========================
# Contact
# =========================
elif section == "Contact":
    st.header("CONTACT")
    st.markdown(f"- GitHub: {PROFILE['github']}")
    st.markdown(f"- Scopus: {PROFILE['scopus']}")
    st.markdown(f"- ORCID: {PROFILE['orcid']}")
    st.caption("Nếu bạn muốn thêm Email/LinkedIn/Website, nói mình các link là mình nhét vào đúng layout.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Profile-style site based on your GitHub README.")
