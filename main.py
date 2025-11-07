from js import document # type: ignore
from pyscript import display  # type: ignore

def compute_gwa(e):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    english = float(document.getElementById("English").value)
    filipino = float(document.getElementById("Filipino").value)
    math = float(document.getElementById("Math").value)
    science = float(document.getElementById("Science").value)
    social = float(document.getElementById("Social").value)
    pe = float(document.getElementById("PE").value)

    total = english + filipino + math + science + social + pe
    gwa = total / 6

    summary = f"""
    <b>ᛝ ɴᴀᴍᴇ:</b> {fname} {lname}<br>
    <b>ᛝ ᴇɴɢʟɪꜱʜ:</b> {english}<br>
    <b>ᛝ ꜰɪʟɪᴘɪɴᴏ:</b> {filipino}<br>
    <b>ᛝ ᴍᴀᴛʜ:</b> {math}<br>
    <b>ᛝ ꜱᴄɪᴇɴᴄᴇ:</b> {science}<br>
    <b>ᛝ ꜱᴏᴄɪᴀʟ ꜱᴛᴜᴅɪᴇꜱ:</b> {social}<br>
    <b>ᛝ ᴘᴇ:</b> {pe}<br><br>
    <b> ༘ ೀ ʏᴏᴜʀ ɢᴇɴᴇʀᴀʟ ᴡᴇɪɢʜᴛᴇᴅ ᴀᴠᴇʀᴀɢᴇ ɪꜱ:</b> {gwa:.2f} ᵎᵎ
    """

    document.getElementById("output").innerHTML = summary