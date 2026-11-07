import asyncio
import os
import shutil

CLIPS = [
    ("abdo_0", "ar-EG-ShakirNeural", "+8%", "-4Hz", "يا صباح الفل يا بيدو، الموقف جاهز والركاب مستنيين السرفيس!"),
    ("abdo_1", "ar-EG-ShakirNeural", "+8%", "-4Hz", "على جنب يا اسطى، لم الأجرة من ورا وافتح الباب للركاب!"),
    ("abdo_2", "ar-EG-ShakirNeural", "+8%", "-4Hz", "وسع كده يا باشا، الأسطى عبده حافظ شوارع المحروسة حتة حتة!"),
    ("sayed_0", "ar-EG-ShakirNeural", "-4%", "-10Hz", "أوردر الكشري والحواوشي سخن وجاهز، طير بيه بالموتوسيكل يا بطل!"),
    ("sayed_1", "ar-EG-ShakirNeural", "-4%", "-10Hz", "ربنا يستر طريقك يا ابني، خلي بالك من إشارات المرور!"),
    ("sayed_2", "ar-EG-ShakirNeural", "-4%", "-10Hz", "أحلى كوباية شاي عالرايق لأجدع سواق في بيدو جيمنج!"),
    ("sherif_0", "ar-EG-ShakirNeural", "+4%", "-8Hz", "اركن على جنب يا كابتن! الدورية محاصراك ومفيش مفر!"),
    ("sherif_1", "ar-EG-ShakirNeural", "+4%", "-8Hz", "كسر الإشارة الحمرا فيه مخالفة، التزم بالنظام يا معلم!"),
    ("sherif_2", "ar-EG-ShakirNeural", "+4%", "-8Hz", "خلاص اتقبض عليك! ادفع الغرامة في القسم وابدأ على نضيف."),
    ("marwan_0", "ar-EG-ShakirNeural", "+12%", "+4Hz", "يا زميلي الأوردر سخن في صندوق الدليفري، وصله بسرعة وهتقبض تبس عالي!"),
    ("marwan_1", "ar-EG-ShakirNeural", "+12%", "+4Hz", "عاش يا بطل! الموتوسيكل بيعدي في الزحمة زي الصاروخ!"),
    ("nadia_0", "ar-EG-SalmaNeural", "+5%", "+2Hz", "وسعوا السكة للإسعاف يا جماعة، رايحين نلحق المصاب فوراً!"),
    ("nadia_1", "ar-EG-SalmaNeural", "+5%", "+2Hz", "نزلني عند الموقف الجاي لو سمحت يا اسطى، الأجرة معاك أهي!"),
    ("nadia_2", "ar-EG-SalmaNeural", "+5%", "+2Hz", "حمد لله على السلامة، الإسعاف وصل والمصاب بقى زي الفل!"),
    ("extra_carjack", "ar-EG-ShakirNeural", "+10%", "+2Hz", "يا نهار أبيض! خد المركبة وجري بيها يا جدعان!"),
    ("extra_injured", "ar-EG-ShakirNeural", "+6%", "+4Hz", "آااه يا رجلي! حد يطلب الإسعاف بسرعة يا أهل الخير!"),
    ("extra_escape", "ar-EG-ShakirNeural", "+4%", "-8Hz", "فلت مننا في الزحمة! ارجعوا للدورية يا رجالة."),
]

async def main():
    import edge_tts
    os.makedirs("www/voices", exist_ok=True)
    os.makedirs("voices", exist_ok=True)
    for clip_id, voice, rate, pitch, text in CLIPS:
        out_path = os.path.join("www/voices", f"{clip_id}.mp3")
        root_voice_path = os.path.join("voices", f"{clip_id}.mp3")
        if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
            print(f"Skipping {out_path} (custom human recording already exists)")
            if not os.path.exists(root_voice_path):
                shutil.copyfile(out_path, root_voice_path)
            continue
        if os.path.exists(root_voice_path) and os.path.getsize(root_voice_path) > 0:
            shutil.copyfile(root_voice_path, out_path)
            print(f"Copied custom recording from {root_voice_path} to {out_path}")
            continue
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(out_path)
        shutil.copyfile(out_path, root_voice_path)
        print(f"Generated {out_path}")

if __name__ == "__main__":
    asyncio.run(main())
