import streamlit as st

# Inisialisasi session
if "page" not in st.session_state:
    st.session_state.page = 1
if "answers" not in st.session_state:
    st.session_state.answers = {}

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

st.title("🧠 Tes Kepribadian")

# Statement 1
if st.session_state.page == 1:
    st.subheader("Pertanyaan 1")
    st.write("Saya orang yang tidak suka basa-basi dan lebih memilih untuk berbicara langsung pada topik pembicaraan.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q1")
    st.session_state.answers["q1"] = answer

    st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 2
elif st.session_state.page == 2:
    st.subheader("Pertanyaan 2")
    st.write("Saya selalu tampil percaya diri.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q2")
    st.session_state.answers["q2"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 3
elif st.session_state.page == 3:
    st.subheader("Pertanyaan 3")
    st.write("Saya merasa tidak nyaman bila sering sendiri.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q3")
    st.session_state.answers["q3"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 4
elif st.session_state.page == 4:
    st.subheader("Pertanyaan 4")
    st.write("Saya merasa belum lancar berkomunikasi dihadapan banyak orang.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q4")
    st.session_state.answers["q4"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 5
elif st.session_state.page == 5:
    st.subheader("Pertanyaan 5")
    st.write("Saya terkesan sigap dan tegas.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q5")
    st.session_state.answers["q5"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 6
elif st.session_state.page == 6:
    st.subheader("Pertanyaan 6")
    st.write("Saya nyaman berada di lingkungan manapun.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q6")
    st.session_state.answers["q6"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 7
elif st.session_state.page == 7:
    st.subheader("Pertanyaan 7")
    st.write("Saya belum aktif mengikuti organisasi/kegiatan dilingkungan tempat tinggal.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q7")
    st.session_state.answers["q7"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 8
elif st.session_state.page == 8:
    st.subheader("Pertanyaan 8")
    st.write("Saya suka bekerja kelompok dan tidak suka kesendirian.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q8")
    st.session_state.answers["q8"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 9
elif st.session_state.page == 9:
    st.subheader("Pertanyaan 9")
    st.write("Kepribadian saya berubah tergantung lawan bicara.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q9")
    st.session_state.answers["q9"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 10
elif st.session_state.page == 10:
    st.subheader("Pertanyaan 10")
    st.write("Saya lebih memilih untuk tetap berada di luar atau belakang layar.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q10")
    st.session_state.answers["q10"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 11
elif st.session_state.page == 11:
    st.subheader("Pertanyaan 11")
    st.write("Saya menikmati lingkungan sosial.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q11")
    st.session_state.answers["q11"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 12
elif st.session_state.page == 12:
    st.subheader("Pertanyaan 12")
    st.write("Saya terkadang tertarik dengan percakapan mendalam dan spesifik.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q12")
    st.session_state.answers["q12"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 13
elif st.session_state.page == 13:
    st.subheader("Pertanyaan 13")
    st.write("Saya tidak selalu tahu harus berkata apa kepada seseorang.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q13")
    st.session_state.answers["q13"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 14
elif st.session_state.page == 14:
    st.subheader("Pertanyaan 14")
    st.write("Saya tidak suka banyak waktu sendiri.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q14")
    st.session_state.answers["q14"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 15
elif st.session_state.page == 15:
    st.subheader("Pertanyaan 15")
    st.write("Saya mudah bergaul dalam kesempatan tertentu.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q15")
    st.session_state.answers["q15"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 16
elif st.session_state.page == 16:
    st.subheader("Pertanyaan 16")
    st.write("Saya akan banyak berpikir sebelum bicara.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q16")
    st.session_state.answers["q16"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 17
elif st.session_state.page == 17:
    st.subheader("Pertanyaan 17")
    st.write("Saya merasa berkembang disekitar orang-orang.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q17")
    st.session_state.answers["q17"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 18
elif st.session_state.page == 18:
    st.subheader("Pertanyaan 18")
    st.write("Saya bisa bekerja secara tim ataupun individu.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q18")
    st.session_state.answers["q18"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 19
elif st.session_state.page == 19:
    st.subheader("Pertanyaan 19")
    st.write("Saya tidak terlalu menyukai berinteraksi sosial karena membuat lelah dan menguras tenaga.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q19")
    st.session_state.answers["q19"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 20
elif st.session_state.page == 20:
    st.subheader("Pertanyaan 20")
    st.write("Saya suka berteman dengan banyak orang.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q20")
    st.session_state.answers["q20"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 21
elif st.session_state.page == 21:
    st.subheader("Pertanyaan 21")
    st.write("Saya menyukai tempat ramai, tapi tetap membutuhkan waktu sendiri.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q21")
    st.session_state.answers["q21"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 22
elif st.session_state.page == 22:
    st.subheader("Pertanyaan 22")
    st.write("Saya sering memikirkan sesuatu sebelum mengerjakannya, sehingga terlihat sedang melamun.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q22")
    st.session_state.answers["q22"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 23
elif st.session_state.page == 23:
    st.subheader("Pertanyaan 23")
    st.write("Saya lebih suka membicarakan suatu isu atau berdiskusi.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q23")
    st.session_state.answers["q23"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("➡️ Selanjutnya", on_click=next_page)

# Statement 24
elif st.session_state.page == 24:
    st.subheader("Pertanyaan 24")
    st.write("Saya terkadang bercerita, terkadang menyimpannya sendiri.")

    answer = st.radio("Jawaban Anda:", ["S = Setuju", "T = Tidak Setuju"], key="q24")
    st.session_state.answers["q24"] = answer

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
    with col2:
        st.button("Selesai ✅", on_click=next_page)

# Halaman 3: Hasil
elif st.session_state.page == 25:
    st.markdown("##### Hasil Tes Kepribadian Anda :")

    q1 = st.session_state.answers.get("q1", "")
    q2 = st.session_state.answers.get("q2", "")
    q3 = st.session_state.answers.get("q3", "")
    q4 = st.session_state.answers.get("q4", "")
    q5 = st.session_state.answers.get("q5", "")
    q6 = st.session_state.answers.get("q6", "")
    q7 = st.session_state.answers.get("q7", "")
    q8 = st.session_state.answers.get("q8", "")
    q9 = st.session_state.answers.get("q9", "")
    q10 = st.session_state.answers.get("q10", "")
    q11 = st.session_state.answers.get("q11", "")
    q12 = st.session_state.answers.get("q12", "")
    q13 = st.session_state.answers.get("q13", "")
    q14 = st.session_state.answers.get("q14", "")
    q15 = st.session_state.answers.get("q15", "")
    q16 = st.session_state.answers.get("q16", "")
    q17 = st.session_state.answers.get("q17", "")
    q18 = st.session_state.answers.get("q18", "")
    q19 = st.session_state.answers.get("q19", "")
    q20 = st.session_state.answers.get("q20", "")
    q21 = st.session_state.answers.get("q21", "")
    q22 = st.session_state.answers.get("q22", "")
    q23 = st.session_state.answers.get("q23", "")
    q24 = st.session_state.answers.get("q24", "")

    # Forward chaining sederhana
    ekstrovert_score = 0
    ambivert_score = 0
    introvert_score = 0
    if q1 == "S = Setuju" and q4 == "S = Setuju" and q7 == "S = Setuju" and q10 == "S = Setuju" and q13 == "S = Setuju" and q16 == "S = Setuju" and q19 == "S = Setuju" and q22 == "S = Setuju":
        ekstrovert_score += 1
    elif q2 == "S = Setuju" and q5 == "S = Setuju" and q8 == "S = Setuju" and q11 == "S = Setuju" and q14 == "S = Setuju" and q17 == "S = Setuju" and q20 == "S = Setuju" and q23 == "S = Setuju":
        ambivert_score += 1
    elif q3 == "S = Setuju" and q6 == "S = Setuju" and q9 == "S = Setuju" and q12 == "S = Setuju" and q15 == "S = Setuju" and q18 == "S = Setuju" and q21 == "S = Setuju" and q24 == "S = Setuju":
        introvert_score += 1

    # Penentuan kepribadian
    if ekstrovert_score == 1:
        result_type = "🌟 Kamu cenderung **Ekstrovert**: aktif, terbuka, dan percaya diri."
        color = "green"
    elif ambivert_score == 1:
        result_type = "⚖️ Kamu termasuk **Ambivert**: seimbang antara dunia luar dan refleksi dalam."
        color = "blue"
    else:
        result_type = "🌙 Kamu cenderung **Introvert**: tenang, reflektif, dan nyaman dalam kesendirian."
        color = "purple"

    st.success(result_type)

    st.markdown("---")
    if st.button("🔄 Mulai Ulang"):
        st.session_state.page = 1
        st.session_state.answers = {}
        st.rerun()

