# Learning Log

## 2026-10-23 — Repo kurulumu ve ilk veri envanteri

### Ne yaptım
- Proje iskeletini kurdum: `data/raw`, `scripts`, `notebooks`, `docs`, sanal ortam (`.venv`) ve git reposu.
- Problem brief'i `docs/00_problem_brief.md` olarak ekledim.
- Olist CSV'lerini `data/raw` altına taşıdım ve `scripts/data_inventory.py` ile 9 tablonun envanterini çıkardım.

### Karşılaştığım sorunlar ve çözümleri
1. **PowerShell ile Bash farkı:** Kurulum komutları Bash içindi, ben Windows PowerShell kullanıyordum.
   `&&`, `touch` ve `ls -la` çalışmadı, bu yüzden `.gitignore` hiç oluşmadı.
   Çözüm: komutları `;` ile ayırdım, dosyaları `Set-Content` ve `New-Item` ile oluşturdum.
2. **`.venv` yanlışlıkla repoya girdi:** İlk commit'i `.gitignore` olmadan attığım için sanal ortamın tamamı GitHub'a gitti.
   `git ls-files` ile fark ettim.
   Öğrendiğim: `.gitignore` sadece henüz takip edilmeyen dosyaları dışarıda bırakır, zaten commit'lenmiş dosyaları takipten çıkarmaz.
   Çözüm: `git rm -r --cached .venv` ile takipten çıkardım, tek commit olduğu için `git commit --amend` ve `git push --force` ile geçmişi de temizledim.
   Not: force push'u sadece kendi başıma çalıştığım branch'te kullanırım. Ortak bir branch'te başkalarının geçmişini bozar.
3. **Kaydedilmemiş dosya:** Problem brief'i doldurduğumu düşünüyordum ama dosya diskte 0 bayt görünüyordu.
   Öğrendiğim: bir dosyanın gerçekten kaydedildiğini `Get-Content` ile doğrulamak.

### Kararlar
- Veri seti repoya eklenmeyecek: hem büyük hem de Kaggle lisansına tabi. README'de indirme talimatı olacak.

###
İlk commit'te sanal ortamı yanlışlıkla repoya gönderdim. `git ls-files` ile fark ettim, `.gitignore`'ın
takip edilen dosyalara etki etmediğini öğrendim ve geçmişi `--amend` ile temizledim.
Force push'un neden sadece kişisel branch'lerde güvenli olduğunu da bu sırada kavradım.

### Sıradaki adım
`docs/01_data_inventory.md` dokümanını yazmak ve müşteri analizinin kodunu notebook'ta yazmak.