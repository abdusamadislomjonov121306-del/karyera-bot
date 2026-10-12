# KaryeraUz — vakansiya boti

osonish.uz'dagi yangi vakansiyalarni avtomatik oladi va har biriga rasm hamda shablon bo'yicha matn tayyorlaydi. Postlar admin tekshiruviga yuboriladi, tasdiqlanganlari Telegram kanaliga joylanadi.

Bot **GitHub Actions**'da bepul va uzluksiz ishlaydi: har ishga tushish oxirida keyingisini o'zi chaqiradi.

## Botda nima bor

- Har bir post **4 ta tugma** bilan keladi:
  - ✅ **Tasdiqlash** — post kanalga chiqadi;
  - ❌ **Rad etish** — post kanalga chiqmaydi;
  - ✏️ **Tahrirlash** — bot so'rov yuboradi, siz unga javob (reply) qilib yangi matnni yuborasiz;
  - 🔄 **Boshqa rasm** — rasmning boshqa varianti chiqadi.
- `/start` buyrug'i pastda doimiy **⚙️ Viloyatlar** tugmasini chiqaradi.
- `/holat` — oxirgi tekshiruv vaqti, ko'rilgan/yuborilgan e'lonlar, xatolar va tasdiq kutayotgan postlar soni.
- Sayt javob bermasa yoki Telegramga yuborib bo'lmasa, bot adminga ⚠️ ogohlantirish yuboradi (soatiga ko'pi bilan 1 marta).
- `/viloyatlar` yoki shu tugma 14 hudud ro'yxatini ochadi: har biri **Ha / Yo'q** ko'rinishida, keyin **💾 Saqlash**. Standart holatda faqat Namangan yoqilgan.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `osonish.py` | osonish.uz'ni o'qiydi: vakansiyalar sahifasi (asosiy manba), sitemap (zaxira), maydonlarni ajratish, viloyatni aniqlash |
| `post.py` | Post matni shabloni |
| `card.py` | Rasm (kartochka) chizish, logotip, soha mavzulari |
| `tg.py` | Telegram Bot API |
| `run.py` | Asosiy sikl: e'lonlarni olish, tugmalar, viloyatlar sozlamasi, tinglash rejimi |
| `fonts/` | Rasm uchun shriftlar (Inter, OFL litsenziyasi) |
| `.github/workflows/main.yml` | GitHub Actions: ishga tushirish, holatni saqlash, o'zini qayta chaqirish |
| `state.json` | Botning xotirasi. Uni bot o'zi yaratadi, **qo'lda o'zgartirmang** |

## Sozlamalar (Settings → Secrets and variables → Actions)

| Turi | Nomi | Qiymati |
|---|---|---|
| Secret | `BOT_TOKEN` | @BotFather bergan token |
| Secret | `ADMIN_CHAT_ID` | Tekshiruvchining Telegram ID'si |
| Variable | `CHANNEL_ID` | `@TESTkaryera` (sinov) yoki `@karyerauznamangan` |
| Variable | `INITIAL_SCAN` | `60` — birinchi ishga tushishda ko'riladigan e'lonlar soni |

## Ishga tushirish va sinov

- **Ishga tushirish:** Actions → KaryeraUz bot → **Run workflow**, maydon bo'sh qolsin. Bir marta bosish kifoya, keyin bot o'zi davom etadi.
- **Bitta e'lonni sinash (Telegramsiz):** Run workflow ni bosib, `test_id` maydoniga vakansiya ID'sini yozing, masalan `116052`.
- **To'xtatish:** Actions → KaryeraUz bot → **⋯ → Disable workflow**.

## Muammolar

| Belgi | Sabab va yechim |
|---|---|
| "chat not found" | Admin botda START bosmagan |
| Xabar kelmayapti | Botga `/holat` yozing: oxirgi tekshiruv vaqti va xatolar ko'rinadi. Javob bermasa, bot to'xtagan |
| Hammasini qaytadan boshlash | `state.json` ni o'chirib, Run workflow ni bosing |

Bot faqat osonish.uz'ning ochiq sahifalarini o'qiydi va `robots.txt` qoidalariga amal qiladi: `/api/` ishlatilmaydi, so'rovlar orasida 1 soniyadan ko'proq kutiladi.
