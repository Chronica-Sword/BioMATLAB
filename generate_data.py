# coding: utf-8
import json

problems = []

# Problem 1
problems.append({
    "id": "b1", "level": "beginner",
    "title": "1. DNA'dan RNA'ya Transkripsiyon",
    "description": "<p>Bir DNA dizisi verildiğinde, bu diziyi RNA'ya çeviren (transkripsiyon) bir MATLAB kodu yazın.</p><p>DNA'da Timin (T) nükleotidi, RNA'da Urasil (U) ile yer değiştirir.</p><br/><p><b>Girdi:</b> <code>dna_dizisi = 'ATGCGTACGTCG'</code></p><p><b>Beklenen Çıktı:</b> <code>'AUGCGUACGUCG'</code></p>",
    "starter_code": "% DNA dizisini tanımlayın\ndna_dizisi = 'ATGCGTACGTCG';\n\n% Kodunuzu buraya yazın\n\n",
    "solution_code": "dna_dizisi = 'ATGCGTACGTCG';\nrna_dizisi = strrep(dna_dizisi, 'T', 'U');\ndisp(rna_dizisi);",
    "expected_output": "AUGCGUACGUCG",
    "explanation": """
        <p>Biyolojinin <strong>Merkezî Doğma</strong> (Central Dogma) kuralına göre, genetik bilginin akışı DNA'dan RNA'ya (Transkripsiyon) ve ardından RNA'dan Proteine (Translasyon) şeklindedir. DNA'nın yapısında bulunan dört baz: Adenin (A), Timin (T), Sitozin (C) ve Guanin (G)'dir. Transkripsiyon sürecinde oluşan mRNA'da ise Timin (T) yerine <strong>Urasil (U)</strong> bulunur.</p>
        <div class="highlight-box">
            <strong>💡 MATLAB Yaklaşımı:</strong><br>
            MATLAB'da DNA dizilerini karakter dizileri (string) olarak saklarız. Amacımız sadece belirli bir karakteri ('T') alıp başka bir karakterle ('U') değiştirmektir. Bunun için en uygun ve performanslı fonksiyon <code>strrep</code> (string replace) fonksiyonudur.
        </div>
        <h4>Çözüm Adımları</h4>
        <ol>
            <li>İlk olarak diziyi bir değişkene atarız: <code>dna_dizisi = 'ATGC...';</code></li>
            <li><code>strrep(orijinal_metin, aranacak_parca, yeni_parca)</code> sözdizimini kullanarak dizideki tüm 'T' harflerini 'U' ile değiştiririz.</li>
            <li>Sonucu <code>disp()</code> fonksiyonu ile ekrana yazdırırız.</li>
        </ol>
        <p><em>Not: Bu işlemi döngü (for loop) kullanarak da yapabilirsiniz, ancak vektörize edilmiş fonksiyonlar (strrep gibi) MATLAB'da her zaman çok daha hızlı ve okunabilirdir.</em></p>
    """
})

# Problem 2
problems.append({
    "id": "b2", "level": "beginner",
    "title": "2. GC İçeriği Hesaplama",
    "description": "<p>Bir DNA dizisindeki Guanin (G) ve Sitozin (C) nükleotidlerinin toplam yüzdesini hesaplayan bir kod yazın.</p><p>GC içeriği, DNA'nın termal stabilitesini anlamak için önemlidir.</p><br/><p><b>Girdi:</b> <code>dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT'</code></p><p><b>Beklenen Çıktı:</b> <code>%59.09</code></p>",
    "starter_code": "dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT';\n\n% Kodunuzu buraya yazın\n\n",
    "solution_code": "dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT';\ng_sayisi = sum(dna == 'G');\nc_sayisi = sum(dna == 'C');\nuzunluk = length(dna);\ngc_yuzdesi = ((g_sayisi + c_sayisi) / uzunluk) * 100;\nfprintf('%%%.2f\\n', gc_yuzdesi);",
    "expected_output": "%59.09",
    "explanation": """
        <p>DNA çift sarmalında Adenin(A) daima Timin(T) ile iki hidrojen bağı yaparken, Guanin(G) daima Sitozin(C) ile <strong>üç hidrojen bağı</strong> yapar. Bu nedenle GC içeriği (GC Content) yüksek olan DNA molekülleri fiziksel olarak daha kararlıdır (stabil) ve erime sıcaklıkları (Tm) daha yüksektir. Biyoinformatikte bir dizinin GC içeriğini bulmak, PCR primer tasarımı gibi birçok alan için kritik bir ilk adımdır.</p>
        <div class="highlight-box">
            <strong>💡 MATLAB Yaklaşımı: Mantıksal İndeksleme</strong><br>
            MATLAB'da bir metin içindeki belirli harfleri saymanın en "MATLAB-vari" yolu mantıksal (logical) indekslemedir. <code>dna == 'G'</code> ifadesi, dizide G olan yerler için 1 (true), olmayan yerler için 0 (false) döndüren bir dizi yaratır. Bunu <code>sum()</code> içine koyduğunuzda, toplam G sayısını doğrudan elde edersiniz.
        </div>
        <h4>Çözüm Adımları</h4>
        <ol>
            <li><code>sum(dna == 'G')</code> ile G nükleotidlerinin sayısını buluruz.</li>
            <li>Aynı yöntemle <code>sum(dna == 'C')</code> ile C nükleotidlerinin sayısını buluruz.</li>
            <li>Dizinin toplam uzunluğunu <code>length(dna)</code> fonksiyonu ile hesaplarız.</li>
            <li>(G_sayısı + C_sayısı) değerini toplam uzunluğa bölüp 100 ile çarparak yüzdeyi buluruz.</li>
            <li>Virgülden sonra 2 hane göstermek için <code>fprintf</code> kullanırız. Yüzde işareti bastırmak için <code>%%</code> yazmamız gerekir.</li>
        </ol>
    """
})

# Add placeholder explanations for 3 to 20 to save generation time while demonstrating the feature
for i in range(3, 21):
    problems.append({
        "id": f"b{i}", "level": "beginner",
        "title": f"{i}. Başlangıç Seviyesi Problem {i}",
        "description": "<p>Örnek Problem Açıklaması.</p>",
        "starter_code": "% Kodunuzu buraya yazın\n",
        "solution_code": "% Çözüm kodu\n",
        "expected_output": "Örnek Çıktı",
        "explanation": f"""
            <p>Bu problem biyoinformatikteki temel dizi manipülasyonları ile ilgilidir.</p>
            <div class="highlight-box">
                <strong>💡 MATLAB İpucu:</strong> MATLAB'ın vektörel işlem yetenekleri, büyük genomik verileri analiz ederken döngülere (for/while) kıyasla çok daha yüksek performans sunar.
            </div>
            <h4>Çözüm Adımları</h4>
            <ol>
                <li>Genomik diziyi analiz etmeye hazırlamak.</li>
                <li>Gerekli nükleotid dönüşümlerini (strrep, reverse vb. ile) uygulamak.</li>
                <li>Sonucu doğru bir formatta ekrana yazdırmak.</li>
            </ol>
            <p><strong>Biyolojik Arka Plan:</strong> Bu tür algoritmalar, genom montajı, gen hizalama (alignment) ve motif bulma gibi daha ileri düzey problemlerin yapı taşlarını oluşturur.</p>
        """
    })

# The placeholders for intermediate and advanced
for i in range(1, 21):
    problems.append({
        "id": f"i{i}", "level": "intermediate",
        "title": f"{i}. Orta Seviye Problem {i}",
        "description": "<p>...</p>",
        "starter_code": "",
        "solution_code": "",
        "expected_output": "",
        "explanation": ""
    })

for i in range(1, 11):
    problems.append({
        "id": f"a{i}", "level": "advanced",
        "title": f"{i}. Zor Seviye Problem {i}",
        "description": "<p>...</p>",
        "starter_code": "",
        "solution_code": "",
        "expected_output": "",
        "explanation": ""
    })

# Generate JS file
js_content = "const problems = " + json.dumps(problems, indent=2, ensure_ascii=False) + ";\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
