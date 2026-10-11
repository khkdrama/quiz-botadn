# 📚 Telegram Test Bot

O'qituvchi va o'quvchilar uchun to'liq avtomatlashtirilgan test boti.

## ✨ Imkoniyatlari

### 👨‍🏫 O'qituvchi uchun (ID: 8974809376):
1. **➕ Bittalab test qo'shish**: Savol, variantlar (A, B, C, D) va to'g'ri javobni interaktiv kiritish.
2. **📥 Bir nechta testni birdaniga qo'shish**: Ko'p sonli savollarni bitta matn xabari orqali avtomatik import qilish.
3. **📋 Testlar ro'yxati**: Hamma testlarni ko'rish va kerak bo'lsa bittalab o'chirish (`🗑 O'chirish` tugmasi).
4. **📊 O'quvchilar natijalari**: Barcha o'quvchilarning ballari, foizlari va kim topshirganini kuzatish.
5. **🔔 Avtomatik bildirishnoma**: O'quvchi testni tugatishi bilanoq o'qituvchiga natijasi yuboriladi.

### 🎓 O'quvchi uchun:
1. **/start** bosadi va "🚀 Testni boshlash" tugmasini tanlaydi.
2. Savollar bittadan keladi va pastida qulay **A, B, C, D** inline tugmalari chiqadi.
3. Test tugashi bilan bot **avtomatik tekshiradi**:
   - Har bir savolga to'g'ri (✅) yoki noto'g'ri (❌) javob berilganini ko'rsatadi.
   - O'quvchi tanlagan javob va to'g'ri javobni solishtirib chiqaradi.
   - Umumiy ball va foizni ko'rsatadi.

---

## 🚀 Ishga tushirish bo'yicha ko'rsatma

### 1. Bot Tokenini kiritish
`config.py` faylini oching va Telegram [@BotFather](https://t.me/BotFather) dan olgan bot tokeningizni yozing:

```python
TEACHER_ID = 8974809376
BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"
```

### 2. Botni ishga tushirish
Terminalda quyidagi buyruqni bering:

```bash
cd quiz_bot
python main.py
```
