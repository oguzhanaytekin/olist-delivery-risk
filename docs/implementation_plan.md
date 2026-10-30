# Implementation Plan: Geç Teslimat Riski (Olist)

Hedef bitiş: Aralık 2026 sonu. Bitirme projesinin yoğun haftalarında tarihler esneyebilir.
Ağırlıklar (%) toplam efora göre tahmindir.

Sahip: **O** = Oğuzhan (junior), **C** = Claude (lead / reviewer)

---

## Faz 0 — Problem çerçeveleme (%5) ✅
- [x] T0.1 Problem brief (`docs/00_problem_brief.md`) — C yazdı, O inceledi
- [x] T0.2 Repo kurulumu, `.gitignore`, sanal ortam — O

## Faz 1 — Veri anlama ve kalite (%15) · 26 Eki – 8 Kas
- [x] T1.1 Veri envanteri betiği (`scripts/data_inventory.py`) — C
- [ ] T1.2 Envanter dokümanı + müşteri analizi notebook'u — O
  - Kabul: `docs/01_data_inventory.md` içinde anahtar, eksik veri ve müşteri bulguları + projeye etkileri
- [ ] T1.3 Temizlik kararları ve uygulaması — O
  - Şehir adı normalizasyonu, konum tablosunda posta kodu önekine göre tekil koordinat,
    eksik tarihli siparişlerin durumu
  - Kabul: kararlar gerekçeleriyle dokümante, temizleme kodu `src/` altında fonksiyon olarak
- [ ] T1.4 Hedef değişkenin oluşturulması — O
  - Kabul: hangi siparişlerin dahil edildiği açık, geç teslimat oranı raporlanmış
- [ ] T1.R Faz review — C

## Faz 2 — Analitik katman / SQL (%20) · 9 – 22 Kas
- [ ] T2.1 Veriyi SQLite'a yükleyen betik — O
- [ ] T2.2 Kohort ve retention analizi (window functions) — O
  - Kabul: "neden churn modeli kurmadık" sorusunu verilerle cevaplayan bir tablo/grafik
- [ ] T2.3 Gecikme analizi: eyalet, kategori, satıcı, zaman bazında — O
- [ ] T2.4 Hipotez testi: gecikme ile yorum puanı ilişkisi — O
  - Kabul: istatistiksel test + etki büyüklüğü, brief'teki hipotez doğrulandı mı?
- [ ] T2.5 Bulgular dokümanı (`docs/02_analytics.md`) — O
- [ ] T2.R Faz review + mülakat soruları — C

## Faz 3 — Modelleme (%25) · 23 Kas – 6 Ara
- [ ] T3.1 Feature listesi ve sızıntı denetimi — O, C onaylar
  - Kabul: her feature için "tahmin anında mevcut mu?" kontrolü yazılı
- [ ] T3.2 Feature engineering: Haversine mesafe, aynı eyalet, kargo ücreti, ürün boyutu, tarih özellikleri — O
- [ ] T3.3 Zaman bazlı train / validation / test ayrımı — O
- [ ] T3.4 Baseline'lar (brief'teki iki kural) — O
- [ ] T3.5 Lojistik regresyon + gradient boosting (LightGBM veya XGBoost) — O
- [ ] T3.6 Deney kaydı: her denemenin parametre ve skorları tek tabloda — O
- [ ] T3.R Faz review + yapay zekâ çıktısı denetleme alıştırması — C

## Faz 4 — Değerlendirme ve iş etkisi (%10) · 7 – 13 Ara
- [ ] T4.1 PR-AUC ve %10 müdahale kapasitesinde yakalama oranı — O
- [ ] T4.2 Eşik seçimi ve maliyet senaryosu — O
- [ ] T4.3 SHAP ile açıklanabilirlik — O
- [ ] T4.4 Hata analizi: model nerede yanılıyor? — O
- [ ] T4.R Faz review — C

## Faz 5 — Servisleştirme (%15) · 14 – 24 Ara
- [ ] T5.1 Model ve ön işleme adımlarını kaydetme (pipeline) — O
- [ ] T5.2 FastAPI `/predict` servisi — O
- [ ] T5.3 Streamlit + Plotly arayüzü: analiz grafikleri ve tahmin ekranı — C iskelet, O içerik
- [ ] T5.4 Temel testler (pytest) — O
- [ ] T5.R Kod review — C

## Faz 6 — Anlatım (%10) · 25 – 31 Ara
- [ ] T6.1 README: problem, veri, yöntem, sonuç, nasıl çalıştırılır — O, C düzenler
- [ ] T6.2 Mimari / akış diyagramı — O
- [ ] T6.3 5 dakikalık proje anlatımı (mülakat versiyonu) — O
- [ ] T6.4 Proje üzerine mock mülakat — C

---

## Sürekli işler (proje boyunca)
- Haftada 2 kez yapay zekâsız, süre tutulan SQL/pandas pratiği
- Her çalışma oturumundan sonra `LEARNING_LOG.md` kaydı
- Her faz sonunda commit + push
