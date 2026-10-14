"""Vakansiyani kanal shabloni bo'yicha post matniga aylantirish (Telegram HTML)."""
import html, re

CHANNEL_LINK = "https://t.me/karyerauznamangan"

def _sched(s):
    """'6/1, 08:00 - 17:00' -> 'haftasiga 6 kun ish, 1 kun dam, 08:00–17:00'"""
    m = re.match(r"\s*(\d)\s*/\s*(\d)\s*,?\s*(.*)", s or "")
    if not m:
        return s or "Kelishiladi"
    t = re.sub(r"\s*-\s*", "–", m.group(3).strip())
    return f"haftasiga {m.group(1)} kun ish, {m.group(2)} kun dam" + (f", {t}" if t else "")

def _edu(s):
    return re.sub(r"\s*\(", " (", s or "Ahamiyatsiz")

def _place(v):
    reg, dist = v.get("region") or "", v.get("district") or ""
    if reg and dist and reg.split()[0].lower() not in dist.lower():
        return f"{reg}, {dist}"
    return dist or reg or "O'zbekiston"

CONTACT_INDENT = ""  # telefon raqami ismdan keyingi qatorda

def build_text(v):
    e = lambda s: html.escape(str(s), quote=False)
    # Bog'lanish: HR menejer / mas'ul shaxs ismi (KATTA harfda), keyingi qatorda telefon raqami
    phones = []
    for ph in [v.get("hr_phone")] + list(v.get("phones") or []):
        ph = re.sub(r"[^\d+]", "", ph or "")
        if ph and ph not in phones:
            phones.append(ph)
    who = (v.get("hr_name") or v.get("contact_name") or "").strip().upper()
    if phones:
        nums = [f"{CONTACT_INDENT}{e(p)}" for p in phones[:2]]
        if who:
            contact_line = f"📞 Bog'lanish: {e(who)}\n" + "\n".join(nums)
        else:
            contact_line = f"📞 Bog'lanish: {e(phones[0])}" + "".join(f"\n{n}" for n in nums[1:])
    else:
        contact_line = f"📞 Bog'lanish: osonish.uz orqali — {e(v['url'])}"
    fields = [
        f"🏢 {e(v.get('org') or '—')}",
        f"📍 {e(_place(v))}",
        f"👥 Bo'sh o'rinlar: {v.get('slots', 1)} ta",
        f"🎓 Ma'lumot: {e(_edu(v.get('education')))}",
        f"⏳ Tajriba: {e((v.get('experience') or 'Talab etilmaydi').replace('-', '–'))}",
        f"💰 Maosh: {e(v.get('salary') or 'Kelishiladi')}",
        f"📋 Ish turi: {e((v.get('employment') or 'doimiy').lower())}",
        f"🕗 Ish tartibi: {e(_sched(v.get('schedule')))}",
        contact_line,
        f"🗓 E'lon sanasi: {e(v.get('date', ''))}",
    ]
    return (f"🎓 <b>{e(v['title'].upper())}</b>\n\n"
            + "\n\n".join(fields)
            + "\n\n\n"
            + "🔗 <b>BIZNI KUZATISHDA DAVOM ETING:</b>\n"
            + f"👉 {CHANNEL_LINK}")
