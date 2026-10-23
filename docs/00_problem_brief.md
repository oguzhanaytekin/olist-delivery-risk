# Problem Brief: Geç Teslimat Riski

## İş problemi
Olist'te bazı siparişler müşteriye söylenen tahmini tarihten sonra teslim ediliyor.
Hipotez: geç teslimat düşük yorum puanına ve müşteri kaybına yol açıyor. (Faz 2'de veriyle doğrulanacak.)

## Karar
Sipariş onaylandığı anda, geç kalma riski yüksek siparişleri işaretlemek.
Operasyon ekibi bu siparişler için satıcıyla iletişime geçebilir, kargoyu hızlandırabilir
veya müşteriyi önceden bilgilendirebilir.

## Tahmin anı
Siparişin onaylandığı an (order_approved_at).
Bu andan SONRA oluşan hiçbir bilgi feature olamaz (ör. kargoya veriliş tarihi, yorum).

## Hedef değişken
Teslim edilmiş siparişlerde: gerçek teslim tarihi > tahmini teslim tarihi ise 1, değilse 0.

## Başarı ölçütü
- Teknik: PR-AUC (sınıflar dengesiz olacağı için accuracy değil)
- İş: belirli bir müdahale kapasitesinde (ör. günlük siparişlerin %10'u) yakalanan geç sipariş oranı

## Baseline
1. "Hiçbir sipariş gecikmez" (Olist'in kendi tahminine güvenmek)
2. Basit kural: müşteri ile satıcı farklı eyaletteyse riskli

## Kapsam dışı
Teslim süresinin gün olarak tahmini (regresyon). İleride eklenebilir.