# coding: utf-8
import json
import re

# Read existing data.js
with open("data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Extract json part
json_str = content.replace("const problems = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

problems = json.loads(json_str)

# The new highly detailed texts (400-600 words each) for Intermediate 1 to 5.
int_data = [
    {
        "id": "i1", "level": "intermediate",
        "title": "1. RNA'dan Proteine Çeviri (Translasyon)",
        "description": "<p>Bir mRNA dizisini (örn: AUGUUUCGA...) alıp standart genetik koda (Kodon Tablosu) göre protein dizisine (Amino asit zincirine) çeviren bir kod yazın.</p><br/><p><b>Girdi:</b> <code>rna = 'AUGUUCUAA'</code></p><p><b>Beklenen Çıktı:</b> <code>MF*</code> (M: Metiyonin, F: Fenilalanin, *: Stop)</p>",
        "starter_code": "% Örnek RNA dizisi\nrna = 'AUGUUCUAA';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "rna = 'AUGUUCUAA';\n% MATLAB Bioinformatics Toolbox'ta nt2aa() fonksiyonu bulunur ancak temel mantık şudur:\nkodonlar = {'AUG', 'UUC', 'UAA'};\namino_asitler = {'M', 'F', '*'};\n\nprotein = '';\nfor i = 1:3:length(rna)-2\n    kodon = rna(i:i+2);\n    indeks = find(strcmp(kodonlar, kodon));\n    if ~isempty(indeks)\n        protein = [protein, amino_asitler{indeks}];\n    end\nend\ndisp(protein);",
        "expected_output": "MF*",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Translasyon ve Genetik Kod)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyolojinin merkezî dogmasının son aşaması, mRNA molekülündeki genetik şifrenin ribozomlar tarafından okunarak proteinlerin sentezlenmesi işlemidir; buna <strong>Translasyon (Çeviri)</strong> adı verilir. DNA veya RNA dört harfli bir alfabe (A, C, G, T/U) kullanırken, proteinler yirmi farklı amino asitten oluşan bir alfabe kullanır. Dört harfli bir alfabeyle yirmi harfli bir alfabeyi eşleştirmek için nükleotidlerin üçlü gruplar halinde okunması gerekir. Bu üçlü nükleotid gruplarına <strong>Kodon</strong> denir.</p>
        <p>4 üzeri 3 hesabıyla toplam 64 farklı kodon kombinasyonu vardır. Bu kombinasyonların 61'i amino asitleri şifrelerken, 3 tanesi (UAA, UAG, UGA) ribozoma durmasını söyleyen <strong>Dur (Stop) Kodonlarıdır</strong>. Translasyon her zaman <strong>AUG (Metiyonin)</strong> kodonu ile başlar. Genetik kodun \"dejeneratif\" (bozulmuş) olması, bir amino asidin birden fazla kodon tarafından şifrelenebileceği anlamına gelir; örneğin Lösin amino asidi altı farklı kodon tarafından şifrelenebilir. Biyoinformatikte protein tahmini (protein prediction) yapılırken mRNA dizisi baştan sona üçerli parçalar halinde taranır ve her bir parça sözlük (dictionary) mantığı ile bir amino aside dönüştürülür. Bu işlem, genomik analizlerde genin kodlayan bölgelerini (eksonları) ve üretilecek proteinin 3 boyutlu yapısını modellemek için atılan ilk teknik adımdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemde elimizde belirli bir nükleotid uzunluğuna sahip (üçün katları şeklinde olan) bir karakter dizisi (string) bulunmaktadır. Amacımız, bu diziyi başından başlayarak 3'lü karakter gruplarına (substring/slice) bölmek ve her bir 3'lü grubu daha önceden tanımlanmış bir harita (map/dictionary) kullanarak karşılık gelen tek harflik amino asit sembolüyle değiştirmektir. Nihai sonuç, elde edilen amino asit sembollerinin yan yana eklenmesiyle oluşan yeni ve çok daha kısa bir karakter dizisidir. Stop kodonlarına gelindiğinde standart olarak '*' (yıldız) sembolü konulur veya çeviri işlemi tamamen durdurulur.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB'da bu tür bir \"Sözlük\" (Dictionary) haritalama işlemi yapmak için <code>containers.Map</code> objesi kullanılabilir. Ancak orta seviyeye yeni geçenler için hücre dizileri (Cell Arrays) ve paralel eşleşme mantığı daha eğitici bir yaklaşımdır. Algoritmanın temeli, indeks atlama (step size) mantığına dayanır. Standart bir <code>for</code> döngüsünde indeksler 1, 2, 3 diye artarken, bu problemde 3'er 3'er atlamamız (1, 4, 7...) gerekir. Her adımda o indeks ve sonraki iki indeks alınarak bir kodon elde edilir. Daha sonra bu kodon, hücre dizisi içindeki referans kodonlarla <code>strcmp</code> kullanılarak aranır. <code>find</code> komutu bu eşleşmenin sıra numarasını döndürür ve bu sıra numarası amino asit dizisinden ilgili harfi çekmek için kullanılır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da hücre dizileri (Cell Arrays) süslü parantez <code>{}</code> ile oluşturulur ve elemanlarına erişmek için yine süslü parantez kullanılır. Eğer normal parantez <code>()</code> kullanırsanız hücrenin içindeki veriyi değil, hücrenin kendisini alırsınız. Bu, MATLAB'da en çok yapılan başlangıç-orta seviye hatalarından biridir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>kodonlar = {'AUG', 'UUC', 'UAA'};</code> : Çevrilecek kodonların listesini bir hücre dizisi (cell array) olarak tanımlar. Gerçek bir uygulamada burada 64 adet kodon bulunmalıdır.</li>
        <li><code>amino_asitler = {'M', 'F', '*'};</code> : Bir önceki hücre dizisiyle tam olarak aynı sıraya sahip, karşılık gelen amino asit sembollerini içeren hücre dizisini tanımlar.</li>
        <li><code>protein = '';</code> : Sentezlenecek olan protein zincirini tutmak için boş bir karakter dizisi (string) başlatılır.</li>
        <li><code>for i = 1:3:length(rna)-2</code> : Döngü 1'den başlar, 3'er adım atarak ilerler. <code>length(rna)-2</code> kısmının sebebi, son kodonu alırken dizinin sınırlarını (index out of bounds) aşmamaktır.</li>
        <li><code>kodon = rna(i:i+2);</code> : O anki indeks <code>i</code> den başlayıp iki fazlasına (örneğin 1'den 3'e) kadar olan karakterleri kesip alarak o adımın kodonunu çıkarır.</li>
        <li><code>indeks = find(strcmp(kodonlar, kodon));</code> : Çıkarılan bu kodonu, referans listemizdeki (kodonlar) tüm elemanlarla karşılaştırır (strcmp) ve eşleşen elemanın numarasını <code>find</code> ile bulur.</li>
        <li><code>if ~isempty(indeks)</code> : Eğer eşleşme bulunduysa (dizi boş değilse) bu bloğa girilir. Gerçek hayatta bozuk verilerde kodon bulunamayabilir, bu kontrol hataları önler.</li>
        <li><code>protein = [protein, amino_asitler{indeks}];</code> : Referans listesinde bulduğumuz sırayı kullanarak <code>amino_asitler</code> dizisinden ilgili amino asidi (süslü parantez ile) çeker ve yatay vektör birleştirme işlemi <code>[]</code> ile protein zincirinin sonuna ekleriz.</li>
        <li><code>disp(protein);</code> : Döngü bitip protein zinciri tamamlandığında sonuç komut satırına bastırılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i2", "level": "intermediate",
        "title": "2. Basit Dizi Hizalama Skoru (Sequence Alignment Scoring)",
        "description": "<p>Aynı uzunluktaki iki diziyi karşılaştırıp Eşleşme (Match) için +1, Eşleşmeme (Mismatch) için -1 ve Boşluk (Gap '-') için -2 puan vererek toplam benzerlik skorunu hesaplayan bir kod yazın.</p><br/><p><b>Girdi:</b> <code>seq1='ATGC-T', seq2='ATCCAT'</code></p><p><b>Beklenen Çıktı:</b> <code>1</code> (A-A:+1, T-T:+1, G-C:-1, C-C:+1, --A:-2, T-T:+1)</p>",
        "starter_code": "seq1 = 'ATGC-T';\nseq2 = 'ATCCAT';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "seq1 = 'ATGC-T';\nseq2 = 'ATCCAT';\nskor = 0;\nfor i = 1:length(seq1)\n    if seq1(i) == '-' || seq2(i) == '-'\n        skor = skor - 2;\n    elseif seq1(i) == seq2(i)\n        skor = skor + 1;\n    else\n        skor = skor - 1;\n    end\nend\ndisp(skor);",
        "expected_output": "1",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Hizalama ve Skorlama Matrisleri)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte iki organizmanın veya iki genin evrimsel olarak ne kadar akraba (homolog) olduğunu bulmanın en temel yolu dizilerini alt alta koyup karşılaştırmaktır. Ancak mutasyonlar (harf değişimi) ve delesyonlar/insersiyonlar (harf kayıpları/eklemeleri) nedeniyle diziler nadiren birebir aynıdır. Bir harfin diğerine dönüşmesi (Mismatch), bir harfin tamamen kaybolmasından (Gap) evrimsel olarak daha olasıdır. Bu nedenle, dizilerin benzerliğini matematiksel olarak modelleyebilmek için bir <strong>Skorlama Sistemi</strong> kurulur.</p>
        <p>Dinamik programlama algoritmalarında (örneğin Needleman-Wunsch ve Smith-Waterman) her bir eşleşmeye (Match) pozitif bir ödül verilirken, her eşleşmeme (Mismatch) ve boşluk (Gap) için sistemden puan düşülür (Ceza - Penalty). Boşluk cezası (Gap Penalty) biyolojik gerçeklikleri yansıtmak adına her zaman mismatch cezasından çok daha büyüktür, çünkü doğada dizinin bir parçasının tamamen silinmesi (indel mutasyonu) çok daha yıkıcıdır. Bu problem, dünyadaki tüm arama motorlarının (BLAST vb.) temelini oluşturan skorlama mekanizmasının en çekirdek halidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Girdi olarak hizalanmış (aralarına tire '-' konarak eşit uzunluğa getirilmiş) iki adet string alıyoruz. Dizileri baştan sona paralel olarak taramamız ve her bir sütundaki durumu analiz etmemiz gerekiyor. Kurallarımız nettir: İki harf aynıysa toplam skora +1 ekle, farklıysa -1 ekle. Eğer iki taraftan birinde boşluk ('-') karakteri varsa, bu ağır bir hatadır ve toplam skordan -2 düş. İşlem bittiğinde elde edilen net sayısal skor, dizilerin benzerlik (homology) derecesini ifade edecektir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemi vektörel indeksleme ile (örneğin <code>sum(seq1==seq2)</code>) çözmek mümkündür, ancak boşluk kontrolü (gap penalty) gibi çok katmanlı if-else koşulları devreye girdiğinde, kodun okunabilirliği ve ileride geliştirilebilir olması adına (dinamik programlama matrislerine hazırlık olarak) <strong>for döngüsü</strong> kullanmak en öğretici yaklaşımdır. Döngü her bir indekse sırasıyla gider ve birikimli (cumulative) bir toplama değişkeni olan <code>skor</code> üzerinden hesabı günceller.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da çoklu if-elseif zincirlerinde sıralama kritiktir. Önceliği yüksek olan ve istisnai durumu temsil eden kontroller (örneğin boşluk '-' olup olmaması) en üstteki <code>if</code> bloğuna yazılmalıdır. Eğer önce karakterlerin farklı olup olmadığını (mismatch) kontrol ederseniz, '-' işaretini de sıradan bir harf gibi algılayıp yanlışlıkla -1 cezası kesebilirsiniz.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>skor = 0;</code> : Analiz boyunca kazanılacak veya kaybedilecek puanların tutulacağı birikimli (accumulator) değişkeni sıfırdan başlatıyoruz.</li>
        <li><code>for i = 1:length(seq1)</code> : Her iki dizi de eşit uzunlukta olduğu için, birinci dizinin başından sonuna kadar adım adım ilerleyecek bir döngü kuruyoruz. İndeks değerini <code>i</code> olarak tutuyoruz.</li>
        <li><code>if seq1(i) == '-' || seq2(i) == '-'</code> : İlk ve en önemli kontrolümüz boşluk kontrolüdür. Dizilerden herhangi birinde o indekste '-' karakteri varsa, mantıksal VEYA (<code>||</code>) operatörü ile bu bloğa girilir.</li>
        <li><code>skor = skor - 2;</code> : Boşluk (Gap) tespit edildiği için mevcut skordan 2 ceza puanı düşülür.</li>
        <li><code>elseif seq1(i) == seq2(i)</code> : Boşluk yoksa ve birinci dizideki karakter ile ikinci dizideki karakter tamamen aynıysa bu bloğa girilir (Match durumu).</li>
        <li><code>skor = skor + 1;</code> : Başarılı eşleşme için skora 1 ödül puanı eklenir.</li>
        <li><code>else</code> : Ne boşluk var ne de karakterler aynı. Geriye kalan tek ihtimal karakterlerin farklı olmasıdır (Mismatch durumu).</li>
        <li><code>skor = skor - 1;</code> : Harf değişimi mutasyonu tespit edildiği için skordan 1 ceza puanı düşülür.</li>
        <li><code>disp(skor);</code> : Tüm dizinin taranması bittikten sonra elde edilen nihai net skor ekrana yazdırılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i3", "level": "intermediate",
        "title": "3. GC Skew (Çarpıklık) Hesabı",
        "description": "<p>Bir DNA dizisi içindeki Guanin ve Sitozin dengesizliğini (G - C) / (G + C) formülü ile hesaplayan bir kod yazın. Bu metrik bakterilerde DNA kopyalama başlangıcını bulmakta kullanılır.</p><br/><p><b>Girdi:</b> <code>dna = 'GGGCCCGG'</code></p><p><b>Beklenen Çıktı:</b> <code>0.25</code> (G=5, C=3 -> 2/8)</p>",
        "starter_code": "dna = 'GGGCCCGG';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'GGGCCCGG';\ng = sum(dna == 'G');\nc = sum(dna == 'C');\ngc_skew = (g - c) / (g + c);\nfprintf('GC Skew: %f\\n', gc_skew);",
        "expected_output": "GC Skew: 0.250000",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (GC Skew ve Replikasyon Orijini)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bakteriyel kromozomlar genellikle dairesel (circular) bir yapıya sahiptir. Hücre bölünmeden önce bu dairesel DNA'nın kopyalanması (replikasyon) gerekir. Kopyalama işlemi kromozomun herhangi bir yerinden başlamaz; <strong>OriC (Origin of Replication)</strong> adı verilen çok spesifik bir noktadan başlar ve iki yöne doğru ilerleyerek <strong>TerC (Terminus)</strong> noktasında son bulur. Biyoinformatikçiler bir bakterinin DNA dizisine bakarak bu OriC noktasının nerede olduğunu bulmak isterler, çünkü bu nokta hücresel mekanizmaların kilit bölgesidir.</p>
        <p>Replikasyon sırasında DNA'nın iki ipliğinden biri (Leading strand) sürekli, diğeri (Lagging strand) ise kesintili kopyalanır. Kesintili kopyalanan iplik tek sarmal halde daha uzun süre kalır ve bu durum Sitozin (C) bazının zamanla deaminasyon geçirerek Urasile, ardından onarım mekanizmalarıyla Timine (T) dönüşmesine (C -> T mutasyonuna) neden olur. Sonuç olarak, OriC'den TerC'ye giden Leading iplikte Guanin (G) sayısı artarken Sitozin (C) sayısı azalır. İşte bir dizideki Guaninlerin Sitozinlere karşı sayısal üstünlüğünü (asimetrisini) ölçen matematiksel formüle <strong>GC Skew (GC Çarpıklığı)</strong> denir. GC Skew değerinin negatiften pozitife sert bir geçiş yaptığı nokta, bakterinin Replikasyon Orijinini (OriC) gösterir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız, verilen karakter dizisindeki mutlak Guanin ve Sitozin sayılarını bulmak, ardından bu sayıları spesifik bir formüle oturtmaktır. Formül: <code>(G Sayısı - C Sayısı) / (G Sayısı + C Sayısı)</code> şeklindedir. Eğer G sayısı C sayısından fazlaysa sonuç pozitif (0 ile 1 arası), C sayısı daha fazlaysa negatif (0 ile -1 arası), eşitlerse tam 0 çıkar. Bu metrik oransal bir göstergedir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB'da daha önce kullandığımız mantıksal dizileme (logical indexing) algoritması G ve C sayılarını bulmak için en hızlı ve en doğru yöntemdir. Dikkat edilmesi gereken nokta, matematiksel işlemler sırasında parantez öncelikleridir. Hem pay (numerator) hem de payda (denominator) parantez içine alınmalıdır. Aksi halde bölme işlemi matematiksel sıraya göre öncelik kazanır ve tamamen yanlış bir sonuç çıkar.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Eğer verilen DNA dizisinde hiç G ve hiç C yoksa (Örneğin dizi 'ATATAT' ise), formülün paydası 0 olur. MATLAB'da sıfıra bölme işlemi (0/0) programı çökertmez ancak <code>NaN</code> (Not a Number) döndürür. İleri düzey yazılımlarda paydaya küçük bir epsilon sabiti (örn: + 1e-10) eklenerek veya if kontrolü yapılarak <code>NaN</code> hatalarının önüne geçilir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>g = sum(dna == 'G');</code> : Dizinin tamamını tarayıp sadece 'G' karakterlerinin olduğu indeksleri 1 yapan mantıksal maskeyi <code>sum</code> ile toplayarak toplam G frekansını elde ediyoruz.</li>
        <li><code>c = sum(dna == 'C');</code> : Aynı şekilde dizideki 'C' karakterlerinin sayısını bulup <code>c</code> değişkenine atıyoruz.</li>
        <li><code>gc_skew = (g - c) / (g + c);</code> : Parantez kullanımına çok dikkat ederek matematiksel formülü uyguluyoruz. Önce fark (pay) bulunuyor, sonra toplam (payda) bulunuyor ve birbirine bölünerek asimetri endeksi hesaplanıyor.</li>
        <li><code>fprintf('GC Skew: %f\\n', gc_skew);</code> : Bulunan sonucu ondalıklı bir sayı (float) olarak ekrana yazdırmak için <code>fprintf</code> ve <code>%f</code> format belirleyicisini kullanıyoruz.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i4", "level": "intermediate",
        "title": "4. Transisyon ve Transversiyon Mutasyonları",
        "description": "<p>Eşit uzunluktaki iki diziyi karşılaştırın. Pürinden Pürine (A <-> G) veya Pirimidinden Pirimidine (C <-> T) olan mutasyon sayısını (Transisyon) bulun.</p><br/><p><b>Girdi:</b> <code>d1='ATGC', d2='GTAC'</code></p><p><b>Beklenen Çıktı:</b> <code>Transisyon: 2</code> (A->G, T->T(Yok), G->A, C->C(Yok))</p>",
        "starter_code": "d1 = 'ATGC';\nd2 = 'GTAC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "d1 = 'ATGC';\nd2 = 'GTAC';\nts = 0;\nfor i = 1:length(d1)\n    b1 = d1(i);\n    b2 = d2(i);\n    if b1 ~= b2\n        if (b1=='A' && b2=='G') || (b1=='G' && b2=='A')\n            ts = ts + 1;\n        elseif (b1=='C' && b2=='T') || (b1=='T' && b2=='C')\n            ts = ts + 1;\n        end\n    end\nend\ndisp(ts);",
        "expected_output": "2",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Mutasyon Türleri)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>DNA üzerinde gerçekleşen tek harflik değişimlere Nokta Mutasyonları (Point Mutations) denir. Bu mutasyonlar biyokimyasal olarak ikiye ayrılır. <strong>Transisyon (Transition)</strong>: İki halkalı yapısı olan pürin bazlarının kendi aralarında (Adenin ile Guanin) veya tek halkalı yapısı olan pirimidin bazlarının kendi aralarında (Sitozin ile Timin) yer değiştirmesidir. <strong>Transversiyon (Transversion)</strong> ise bir pürinin bir pirimidine (veya tam tersi) dönüşmesidir.</p>
        <p>Matematiksel olarak bakıldığında, 4 farklı baz olduğu için toplam 12 çeşit mutasyon ihtimali vardır. Bunların 4 tanesi Transisyon, 8 tanesi Transversiyondur. Yani rastgele bir mutasyonun transversiyon olma ihtimali 2 kat daha fazladır. Ancak biyolojik doğada, moleküler yapının boyutunu (halka sayısını) değiştirmeyen Transisyon mutasyonları çok daha kolay gerçekleşir ve DNA onarım mekanizmalarından daha kolay kaçar. Bu nedenle genom dizilerinde transisyonlar, transversiyonlardan çok daha sık görülür. Bu iki mutasyonun birbirine oranının (Ts/Tv oranı) hesaplanması, iki gen arasındaki evrimsel mesafeyi daha doğru ölçmek için (örneğin Kimura'nın 2 Parametreli Modeli) kritik bir parametredir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız eşit uzunlukta iki stringi yan yana getirmek ve her bir harfi paralel olarak karşılaştırmaktır. Sadece harflerin farklı (mismatch) olduğu durumları bulmakla kalmayıp, bu farkın karakterinin ne olduğunu da (A'dan G'ye mi yoksa A'dan C'ye mi) belirlemeliyiz. Sadece Transisyon kurallarına uyan (A<->G veya C<->T) değişimlerin sayısını artırmamız istenmektedir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Vektörel operatörlerle bu işlemi yapmak karmaşık mantıksal matrisler gerektirecektir. Orta seviyede daha okunabilir bir kod yazmak için döngü (for loop) ve karar yapıları (if/elseif) iç içe kullanılır. Algoritmik olarak kodu hızlandırmak için ilk şart olarak \"Karakterler birbirine eşit değil mi?\" (<code>~=</code>) sorusunu sormak çok verimlidir. Eğer harfler aynıysa karmaşık karakter karşılaştırmalarına girmeden döngü hemen sonraki adıma atlar.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da mantıksal kontroller yaparken <code>&&</code> (kısa devre VE) ve <code>||</code> (kısa devre VEYA) operatörlerini kullanmak performansı artırır. Eğer <code>b1=='A'</code> şartı yanlışsa (false), <code>&&</code> operatörü yanındaki ikinci şarta (<code>b2=='G'</code>) hiç bakmaz ve işlemi anında sonlandırır. Bu kısa devre (short-circuit) özelliği, binlerce iterasyon süren döngülerde çok büyük bir zaman tasarrufu sağlar.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>ts = 0;</code> : Transisyon mutasyonlarını sayacak sayacı (counter) sıfırdan başlatırız.</li>
        <li><code>for i = 1:length(d1)</code> : Her iki dizi için de geçerli olan bir indeks sayacı (i) ile baştan sona ilerleyen bir döngü kurarız.</li>
        <li><code>b1 = d1(i); b2 = d2(i);</code> : İleride kodu daha okunaklı kılmak için (sürekli dizi indeksi yazmamak adına), o anki karakterleri b1 ve b2 isimli geçici skaler değişkenlere atıyoruz.</li>
        <li><code>if b1 ~= b2</code> : Yalnızca harflerin farklı (mutasyonlu) olduğu durumlarda çalışacak filtre yapısı.</li>
        <li><code>if (b1=='A' && b2=='G') || (b1=='G' && b2=='A')</code> : Eğer mutasyon A'dan G'ye VEYA G'den A'ya ise bu bir Pürin transisyonudur. Sayaç <code>ts = ts + 1</code> ile artırılır. Parantezlerle gruplandırma, operatör önceliği açısından hayati önem taşır.</li>
        <li><code>elseif (b1=='C' && b2=='T') || (b1=='T' && b2=='C')</code> : Eğer mutasyon C'den T'ye VEYA T'den C'ye ise bu bir Pirimidin transisyonudur. Sayaç yine artırılır.</li>
        <li>Tüm işlemler bittikten sonra döngü sonlanır ve toplam transisyon sayısı ekrana basılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i5", "level": "intermediate",
        "title": "5. K-mer Frekansı Bulma",
        "description": "<p>Büyük bir DNA dizisindeki tüm olası 3 harfli (k=3) kombinasyonları (K-mer'leri) çıkaran ve her birinin kaç kez geçtiğini bulan bir program yazın. Bunu bir For döngüsü ile yapın.</p><br/><p><b>Girdi:</b> <code>dna = 'ATGCAT'</code></p><p><b>Beklenen Çıktı:</b> <code>ATG:1, TGC:1, GCA:1, CAT:1</code></p>",
        "starter_code": "dna = 'ATGCAT';\nk = 3;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGCAT';\nk = 3;\n% İleri düzey optimizasyonlarda Dictionary (containers.Map) kullanılır.\nfor i = 1:length(dna)-k+1\n    kmer = dna(i:i+k-1);\n    fprintf('%s ', kmer);\nend\nfprintf('\\n');",
        "expected_output": "ATG TGC GCA CAT ",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (K-mer'ler ve Genom Montajı)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte uzun bir diziyi analiz ederken, o diziyi belirli bir <strong>k</strong> uzunluğunda ardışık kısa parçalara bölme işlemine k-mer analizi denir. Örneğin <code>ATGC</code> dizisinde k=2 (dimer) ise elde edilecek k-merler AT, TG ve GC olur. K-mer'lerin kullanım alanı biyoinformatikte devasadır.</p>
        <p>Modern genom sekanslama cihazları (Illumina vb.) bütün bir insan genomunu tek seferde okuyamazlar. Bunun yerine genomu 100-150 harflik milyonlarca kısa parçaya (reads) bölerek okurlar. Bu kısa parçaları alıp bir yapboz gibi birleştirerek tekrar bütün bir insan genomu elde etme işlemine <strong>Genom Montajı (Genome Assembly)</strong> denir. Montaj algoritmalarının kalbinde De Bruijn Grafikleri yatar. De Bruijn grafikleri, bu kısa parçaları k-mer'lere ayırarak aralarındaki örtüşmeleri (overlap) matematiksel bir ağ haritasına dönüştürür. Hangi k-mer'in tüm genomda kaç kez geçtiğinin frekansı, genomun tekrar eden dizilerini (repetitive sequences) ve kalitesini bulmak için kritik bir özet (fingerprint) verisidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Problemimiz çok nettir: Bize bir karakter dizisi ve bir k değeri (örneğin 3) verilir. Amacımız dizinin en başından başlayıp 3'lü karakterler koparmak, ardından pozisyonumuzu (indeksi) 1 karakter yana kaydırıp (sliding window) bir 3'lü karakter daha koparmaktır. Bu işlem, dizinin sonuna geldiğimizde koparacak 3 karakter kalmayana kadar devam etmelidir. Bu çözümde k-merlerin listesini üreteceğiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bir pencereyi dizi üzerinde kaydırmak (Sliding Window Algorithm) için for döngüsü en şeffaf yöntemdir. Buradaki en tehlikeli kısım, <strong>indeks sınırıdır (Index Out of Bounds)</strong>. Eğer dizimiz 6 karakterliyse ve biz 3 karakterlik k-mer'ler alıyorsak, penceremizin sol ucu en son 4. indekste durabilir (4, 5, 6'yı alır). Eğer pencere 5. indekse geçerse, dışarıda sadece 6 kalmıştır ancak sistem 3 karakter almak isteyeceği için boşlukta (yoklukta) okuma yapmaya çalışıp hata vererek çöker. Sınırı <code>uzunluk - k + 1</code> formülü ile matematiksel olarak güvenceye almak şarttır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Tüm olasılıkları sayıp bir frekans tablosu yaratmak isteseydik MATLAB'ın modern veri yapısı olan <code>dictionary</code> (veya eski sürümlerde <code>containers.Map</code>) objesini kullanmamız gerekirdi. Bu veri yapısında her yeni çıkan k-mer, sözlüğe Anahtar (Key) olarak atılır ve Değeri (Value) 1 artırılırdı.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>k = 3;</code> : K-mer büyüklüğü belirlenir (Trimers).</li>
        <li><code>for i = 1:length(dna)-k+1</code> : Döngünün sınır koşulu dinamik olarak belirlenir. Toplam uzunluk (6) - k (3) + 1 = 4. Yani döngü i=1, 2, 3 ve 4 için çalışır, 5'te durur.</li>
        <li><code>kmer = dna(i:i+k-1);</code> : İşte kayan pencerenin kendisi budur. <code>i</code> başlangıç indeksi, <code>i+k-1</code> bitiş indeksidir. Örneğin i=2 için (2 : 2+3-1) -> (2 : 4) arasındaki harfleri dilimler.</li>
        <li><code>fprintf('%s ', kmer);</code> : Elde edilen 3 harfli k-mer'i yanına bir boşluk koyarak yatay düzlemde ekrana basar. Dizinin tüm k-mer'leri okunaklı bir şekilde listelenmiş olur.</li>
    </ul>
</div>
        """
    }
]

# Update the corresponding placeholders in the problems list
updated = False
for new_prob in int_data:
    for i, p in enumerate(problems):
        if p.get("id") == new_prob["id"]:
            problems[i] = new_prob
            updated = True
            break

js_content = "const problems = " + json.dumps(problems, indent=2, ensure_ascii=False) + ";\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
