import streamlit as st
import math

st.title("📊 Notenrechner (mit + / −)")

noten_map = {
    "1+": 0.75, "1": 1.0, "1-": 1.25,
    "2+": 1.75, "2": 2.0, "2-": 2.25,
    "3+": 2.75, "3": 3.0, "3-": 3.25,
    "4+": 3.75, "4": 4.0, "4-": 4.25,
    "5+": 4.75, "5": 5.0, "5-": 5.25,
    "6": 6.0
}

def parse_noten(text):
    noten = []
    for n in text.split(","):
        n = n.strip()
        if n in noten_map:
            noten.append(noten_map[n])
    return noten

st.write("### 📝 Arbeiten (40 %)")
arbeiten_input = st.text_input(
    "z. B. 2, 3+, 1-",
    ""
)

st.write("### 🗣️ Mündlich (60 %)")
muendlich_input = st.text_input(
    "z. B. 2+, 2, 3-",
    ""
)

arbeiten = parse_noten(arbeiten_input)
muendlich = parse_noten(muendlich_input)

if arbeiten and muendlich:
    avg_arbeiten = sum(arbeiten) / len(arbeiten)
    avg_muendlich = sum(muendlich) / len(muendlich)

    gesamt = avg_arbeiten * 0.4 + avg_muendlich * 0.6
    endnote = math.floor(gesamt + 0.5)

    st.write("---")
    st.write(f"📘 **Durchschnitt Arbeiten:** {avg_arbeiten:.2f}")
    st.write(f"🗣️ **Durchschnitt Mündlich:** {avg_muendlich:.2f}")
    st.write(f"📈 **Gesamtdurchschnitt:** {gesamt:.2f}")
    st.success(f"🎓 **Endnote (gerundet): {endnote}**")
else:
    st.info("Bitte gültige Noten eingeben (z. B. 3+, 2-, 4).")
