# coding: utf-8
import json

with open("data.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("const problems = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

problems = json.loads(json_str)

int_data = [
    {
        "id": "i6", "level": "intermediate",
        "title": "6. Kayan Pencere ile Yerel GC İçeriği Analizi",
        "description": "<p>Uzun bir DNA dizisinin tamamının değil, belirli bir pencere (window) boyutuyla (örn: k=10) dizinin üzerinden kayarak (sliding window) her bir bölgenin GC içeriğini hesaplayan ve bunları bir diziye kaydeden bir program yazın.</p><br/><p><b>Girdi:</b> <code>dna = 'ATGCGCATATCGATC', k=5</code></p><p><b>Beklenen Çıktı:</b> <code>[60.0, 80.0, 80.0, 60.0, 40.0, 20.0, 20.0, 40.0, 40.0, 60.0, 40.0]</code> (Her bir 5 harflik parçanın GC yüzdesi)</p>",
        "starter_code": "dna = 'ATGCGCATATCGATC';\nk = 5;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGCGCATATCGATC';\nk = 5;\nuzunluk = length(dna) - k + 1;\ngc_oranlari = zeros(1, uzunluk);\n\nfor i = 1:uzunluk\n    pencere = dna(i:i+k-1);\n    g = sum(pencere == 'G');\n    c = sum(pencere == 'C');\n    gc_oranlari(i) = ((g + c) / k) * 100;\nend\ndisp(gc_oranlari);",
        "expected_output": "    60    80    80    60    40    20    20    40    40    60    40",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Genomik Bölgeler ve GC Adacıkları)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyolojide, milyonlarca veya milyarlarca baz çiftinden oluşan devasa bir genomun tek bir ortalama GC içeriğine sahip olduğunu söylemek yanıltıcıdır. Genomlar homojen değildir; bazı bölgeler (örneğin protein kodlayan genlerin başlangıç bölgeleri olan Promotörler) GC açısından inanılmaz derecede zenginken (CpG Adacıkları - CpG Islands), kodlanmayan bölgeler (çöp DNA veya intronlar) genellikle AT açısından zengindir. Bu nedenle biyoinformatikçiler genomun tamamına tek bir yüzde vermek yerine, genomu küçük pencerelere (sliding windows) bölerler. Örneğin, kromozom üzerinde 1000 bazlık bir pencere açılır, o pencerenin GC oranı hesaplanır, sonra pencere 10 baz yana kaydırılarak tekrar hesaplanır. Bu veriler daha sonra bir çizgi grafiğine dökülür ve genomun GC haritası çıkarılır. Promotörleri, gen sınırlarını ve epigenetik metilasyon hedeflerini bulmanın en standart yolu bu yerel dalgalanmaları görselleştirmektir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemde bir ana dizi ve bir <code>k</code> (pencere boyutu) parametresi verilmektedir. Amacımız, başlangıçtan itibaren <code>k</code> uzunluğunda bir alt dizi (slice) almak, bu alt dizinin GC içeriğini (yüzde olarak) hesaplamak ve bu değeri sayısal bir dizinin (array/vector) ilk elemanı olarak kaydetmektir. Daha sonra başlangıç noktasını bir adım (1 nükleotid) yana kaydırıp işlemi tekrarlamamız gerekir. Sonuç olarak, ana diziden daha kısa, ancak genomun yerel karakteristiğini gösteren bir sayısal vektör elde etmeliyiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Kayan pencere (Sliding Window) algoritmaları için her zaman bir For döngüsü kullanılır. Döngünün güvenli bir şekilde çalışabilmesi ve son pencerenin dizinin dışına (Index Out of Bounds) taşmaması için sınır koşulunu <code>uzunluk - k + 1</code> olarak belirlemek zorundayız. Ayrıca MATLAB'da performansı artırmanın en büyük kuralı <strong>Ön Tahsis (Preallocation)</strong> yapmaktır. Döngü içinde sürekli boyutu artan bir dizi kullanmak yerine, en baştan <code>zeros()</code> komutuyla sonuçların tutulacağı diziyi sıfırlarla doldurarak bellekte yer ayırmak, kodu binlerce kat hızlandırabilir.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da <code>gc_oranlari(end+1) = deger;</code> şeklinde bir kullanım (diziyi her adımda büyütmek) küçük verilerde çalışsa da, büyük genomik dosyalarda inanılmaz bir performans düşüşüne (darboğaz - bottleneck) neden olur. Çünkü sistem her adımda diziyi silip daha büyük bir boyutta belleğe yeniden yazar. Her zaman döngüden önce <code>zeros(1, n)</code> kullanarak bellek ayırın.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>uzunluk = length(dna) - k + 1;</code> : Kaç adet pencere hesaplayacağımızı (döngünün kaç tur atacağını) önceden matematiksel olarak buluruz.</li>
        <li><code>gc_oranlari = zeros(1, uzunluk);</code> : Ön tahsis (Preallocation) işlemi yaparız. Bellekte içi sıfırlarla dolu, 1 satır ve 'uzunluk' kadar sütunu olan yatay bir vektör yaratırız.</li>
        <li><code>for i = 1:uzunluk</code> : Güvenli sınırımıza kadar ilerleyecek döngüyü kurarız.</li>
        <li><code>pencere = dna(i:i+k-1);</code> : Döngünün o anki konumundan başlayarak <code>k</code> kadar harfi kesip alır ve geçici bir değişkene atarız. Örneğin i=1 ve k=5 ise 1'den 5'e kadar (1:5) alınır. i=2 ise (2:6) alınır.</li>
        <li><code>g = sum(pencere == 'G');</code> ve <code>c = sum(pencere == 'C');</code> : Sadece o anki küçük pencerenin içindeki G ve C nükleotidlerini sayarız.</li>
        <li><code>gc_oranlari(i) = ((g + c) / k) * 100;</code> : O pencerenin GC oranını hesaplar ve doğrudan sonuç dizimizin i. indeksine yazarız. Böylece sıfırlar sırasıyla gerçek oranlarla yer değiştirir.</li>
        <li><code>disp(gc_oranlari);</code> : Tüm dizinin GC haritasını gösteren sayısal vektörü ekrana basarız.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i7", "level": "intermediate",
        "title": "7. Needleman-Wunsch Algoritması: Matris İlklendirme",
        "description": "<p>İki DNA dizisini hizalamak için kullanılan Dinamik Programlama (Dynamic Programming) matrisinin ilk satırını ve ilk sütununu Boşluk Cezası (Gap Penalty = -2) kullanarak eksi değerlerle dolduran (Initialization) kodu yazın.</p><br/><p><b>Girdi:</b> <code>seq1 = 'ATC', seq2 = 'AGC', gap = -2</code></p><p><b>Beklenen Çıktı:</b> İlk satırı (0, -2, -4, -6) ve ilk sütunu (0, -2, -4, -6) olan, geri kalanı 0 olan 4x4 boyutunda bir matris.</p>",
        "starter_code": "seq1 = 'ATC';\nseq2 = 'AGC';\ngap_penalty = -2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "seq1 = 'ATC';\nseq2 = 'AGC';\ngap_penalty = -2;\n\ns1_len = length(seq1);\ns2_len = length(seq2);\n\n% Boyutları kelimelerden 1 fazla olan sıfır matrisi (M+1 x N+1)\nmatris = zeros(s1_len + 1, s2_len + 1);\n\n% İlk satırı (seq2'ye karşılık) boşluk cezası ile doldurma\nfor j = 2:s2_len + 1\n    matris(1, j) = matris(1, j-1) + gap_penalty;\nend\n\n% İlk sütunu (seq1'e karşılık) boşluk cezası ile doldurma\nfor i = 2:s1_len + 1\n    matris(i, 1) = matris(i-1, 1) + gap_penalty;\nend\n\ndisp(matris);",
        "expected_output": "     0    -2    -4    -6\n    -2     0     0     0\n    -4     0     0     0\n    -6     0     0     0",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Global Hizalama ve Dinamik Programlama)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte iki diziyi uçtan uca hizalamak (Global Alignment) için kullanılan en meşhur yöntem <strong>Needleman-Wunsch Algoritmasıdır</strong> (1970). Bu algoritma, uzun diziler arasındaki en optimal eşleşmeyi bulmak için Dinamik Programlama (Dynamic Programming) adlı bilgisayar bilimleri konseptini kullanır. Dinamik programlama, büyük bir problemi daha küçük alt problemlere böler, alt problemlerin sonuçlarını bir tabloda (Matris) saklar (memoization) ve büyük problemi çözerken aynı şeyleri tekrar tekrar hesaplamak yerine tablodaki hazır sonuçları kullanır.</p>
        <p>Bu matrisin sol üst köşesi (0,0 noktası) hizalamanın başlangıç noktasıdır. Algoritmanın ilk adımı <strong>Matris İlklendirme (Initialization)</strong> aşamasıdır. İlk satır ve ilk sütun, dizilerden birinin diğerindeki ardışık boşluklarla (gaps) hizalandığı en kötü senaryoyu temsil eder. Bu nedenle ilk satır ve sütun, boşluk cezası (Gap Penalty) kadar düzenli olarak azalan negatif değerlerle doldurulur. Bu ilklendirme yapılmadan matrisin iç kısımları (çapraz eşleşmeler) doğru bir şekilde hesaplanamaz. Bu, algoritmanın temel taşıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>İki dizi alacağız. Birinci dizinin uzunluğuna <code>M</code>, ikinci dizinin uzunluğuna <code>N</code> diyelim. Bize boyutları <code>(M+1) x (N+1)</code> olan boş bir matris (ızgara) gereklidir. Ekstra \"+1\" hücresi, hizalamaya başlamadan önceki başlangıç durumu (sol üst köşe) içindir. Amacımız bu matrisin 1. satırındaki hücreleri 0, -2, -4, -6 şeklinde ve 1. sütunundaki hücreleri 0, -2, -4, -6 şeklinde (boşluk cezası -2 olduğu için) sistematik olarak doldurmaktır. İç hücreler sıfır kalmalıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB bir matris laboratuvarıdır ve bu tür iki boyutlu ızgara işlemleri için dünyadaki en uygun dildir. <code>zeros()</code> fonksiyonu ile iki boyutlu matris oluşturulur. MATLAB indeksleri 1'den başladığı için, sol üst köşe (1,1) hücresi olur. İlk satırı doldurmak için bir for döngüsü kurulur ve her hücre, kendinden bir önceki hücrenin değerine boşluk cezası eklenerek hesaplanır. İlk sütun için de aynı işlemin sütun versiyonu yapılır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da çok boyutlu dizilere (matrislere) erişirken <code>matris(satır, sütun)</code> sırası (Row-Major mantığı) kullanılır. Bu kuralı karıştırmak eksenlerin yer değiştirmesine (Transpoz alınmış gibi görünmesine) yol açar. Her zaman önce Y ekseni (satır), sonra X ekseni (sütun) yazılır.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>s1_len = length(seq1);</code> : İlk dizinin uzunluğunu alıyoruz (M).</li>
        <li><code>matris = zeros(s1_len + 1, s2_len + 1);</code> : Boyutları dizilerin uzunluğundan 1 büyük olan (4x4) ve içi tamamen sıfırlarla dolu bir matris yaratıyoruz. Köşe <code>matris(1,1)</code> otomatik olarak 0 olmuş olur.</li>
        <li><code>for j = 2:s2_len + 1</code> : İlk <strong>satırda</strong> sağa doğru ilerleyeceğimiz için sütun indeksini (j) 2'den başlatıp sona kadar götürüyoruz.</li>
        <li><code>matris(1, j) = matris(1, j-1) + gap_penalty;</code> : 1. satırın j. sütunundaki değeri bulmak için, solundaki hücrenin (1, j-1) değerini alır ve üzerine -2 ekler. Bu (0, -2, -4, -6) serisini oluşturur.</li>
        <li><code>for i = 2:s1_len + 1</code> : İlk <strong>sütunda</strong> aşağı doğru ineceğimiz için satır indeksini (i) 2'den başlatıyoruz.</li>
        <li><code>matris(i, 1) = matris(i-1, 1) + gap_penalty;</code> : i. satırın 1. sütunundaki değeri bulmak için, bir üstteki (i-1, 1) hücrenin değerini alır ve üzerine -2 ekler. Bu da aşağıya doğru aynı seriyi oluşturur.</li>
        <li><code>disp(matris);</code> : İlklendirilmiş (Initialized) Needleman-Wunsch matris iskeleti ekrana yazdırılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i8", "level": "intermediate",
        "title": "8. Jaccard Benzerlik İndeksi (K-mer Kümeleri İle)",
        "description": "<p>İki farklı DNA dizisi veriliyor. Bu dizilerdeki tüm 2'li k-merleri (dimerleri) çıkarın ve bu iki k-mer kümesi arasındaki Jaccard Benzerlik İndeksini (Kesişim / Birleşim) hesaplayın.</p><br/><p><b>Girdi:</b> <code>d1='ATGC', d2='ATCC'</code></p><p><b>Beklenen Çıktı:</b> <code>0.2000</code> (d1={AT, TG, GC}, d2={AT, TC, CC}. Kesişim: {AT} (1 adet). Birleşim: {AT, TG, GC, TC, CC} (5 adet). Sonuç: 1/5 = 0.2)</p>",
        "starter_code": "d1 = 'ATGC';\nd2 = 'ATCC';\nk = 2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "d1 = 'ATGC';\nd2 = 'ATCC';\nk = 2;\n\nkmerler1 = {};\nfor i=1:length(d1)-k+1\n    kmerler1{end+1} = d1(i:i+k-1);\nend\n\nkmerler2 = {};\nfor i=1:length(d2)-k+1\n    kmerler2{end+1} = d2(i:i+k-1);\nend\n\n% Eşsiz (Unique) kümeler oluşturma\nkume1 = unique(kmerler1);\nkume2 = unique(kmerler2);\n\nkesisim = intersect(kume1, kume2);\nbirlesim = union(kume1, kume2);\n\njaccard = length(kesisim) / length(birlesim);\nfprintf('Jaccard İndeksi: %f\\n', jaccard);",
        "expected_output": "Jaccard İndeksi: 0.200000",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Küme Teorisi ve Hizalamasız Yöntemler)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte iki devasa genomun (örneğin iki farklı bakteri türünün 5 milyon harflik genomlarının) birbirine ne kadar benzediğini bulmak için standart hizalama algoritmaları (Needleman-Wunsch gibi) kullanmak aylar süren hesaplama gücü (O(N^2) karmaşıklığı) gerektirir. Bu kadar büyük veriler için hizalama yapmadan (Alignment-free) hızlı benzerlik bulma yöntemleri geliştirilmiştir. Bunun en meşhur yolu <strong>MinHash</strong> algoritmaları ve <strong>Jaccard Benzerlik İndeksi</strong>'dir.</p>
        <p>Yöntem oldukça zekicedir: Her iki genom da küçük parçalara (K-mer'lere) bölünür. Genomun harf sırası tamamen unutulur ve sadece k-mer'lerden oluşan bir \"kelime torbası\" (Bag of words) veya Matematiksel Küme (Set) elde edilir. Ardından bu iki kümenin Jaccard İndeksi hesaplanır. Jaccard İndeksi, iki kümenin kesişimindeki (ortak olan) eleman sayısının, kümelerin birleşimindeki (toplam benzersiz) eleman sayısına bölünmesiyle bulunur. Sonuç 0 (hiç benzemiyorlar) ile 1 (birebir aynılar) arasında bir olasılık değeridir. Bu yöntem, metagenomik analizlerde tür tanımlama için saniyeler içinde çalışır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize iki karakter dizisi verilmiştir. Öncelikle her iki dizi için ayrı ayrı kayan pencere (sliding window) yöntemiyle k=2 boyutunda parçalar çıkarıp bunları listelemeliyiz. Daha sonra bu listeleri kümelere (set) dönüştürmeliyiz; yani tekrar eden parçaları silerek her parçanın sadece bir kez görünmesini sağlamalıyız (Unique işlemi). Son olarak MATLAB'ın küme işlemleri operatörlerini kullanarak ortak elemanları ve toplam elemanları sayıp, bu iki sayıyı birbirine bölerek indeksi vermeliyiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB, karakter dizilerini (string/char) listelemek için Hücre Dizilerini (Cell Arrays) kullanır. Boş bir hücre dizisi (<code>{}</code>) oluşturup k-merleri içine atarız. Sonra MATLAB'ın yerleşik Küme Teorisi (Set Theory) fonksiyonları devreye girer. <code>unique()</code> fonksiyonu bir dizideki benzersiz (tekrarsız) elemanları bırakır, <code>intersect()</code> iki kümenin kesişimini bulur, <code>union()</code> ise birleşimini (herkeste olan her şeyin tekil bir listesini) çıkarır. Bu matematiksel fonksiyonlar olmasaydı iç içe geçmiş karmaşık döngüler yazmamız gerekecekti.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB 2016 sonrasında gelen yeni <code>string</code> veri tipini kullanırsanız, hücre dizilerine <code>{}</code> gerek kalmaz, normal bir vektör (array) gibi <code>[]</code> string dizileri kullanabilirsiniz. Küme fonksiyonları (intersect, union) her iki formata da mükemmel uyum sağlar.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>kmerler1 = {};</code> : Birinci diziye ait k-mer'leri depolamak için boş bir hücre dizisi tanımlanır.</li>
        <li><code>for ... kmerler1{end+1} = d1(i:i+k-1);</code> : Önceki problemlerde gördüğümüz kayan pencere mantığı ile dizi parçalanır ve her parça hücre dizisinin sonuna (<code>end+1</code>) eklenir.</li>
        <li>Aynı for döngüsü ikinci dizi (<code>d2</code>) için de çalıştırılır.</li>
        <li><code>kume1 = unique(kmerler1);</code> : Bir k-mer dizide 10 kez de geçse, küme (set) mantığına göre elemanların eşsiz olması gerekir. Tekrar edenler silinir.</li>
        <li><code>kesisim = intersect(kume1, kume2);</code> : Her iki kümede de bulunan ortak k-mer'lerin (Kesişim) yeni bir dizisi çıkarılır.</li>
        <li><code>birlesim = union(kume1, kume2);</code> : Her iki kümedeki tüm elemanların benzersiz olarak birleştirildiği (Birleşim) yeni bir dizi çıkarılır.</li>
        <li><code>jaccard = length(kesisim) / length(birlesim);</code> : Jaccard formulü olan Kesişim uzunluğu / Birleşim uzunluğu oranı hesaplanarak sonuç yazdırılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i9", "level": "intermediate",
        "title": "9. DNA Dizisinde En Uzun Tekrar Eden Alt Dizi",
        "description": "<p>Bir DNA dizisi içinde birbiriyle örtüşmeyen (non-overlapping) ve en az iki kez tekrar eden en uzun alt diziyi (Longest Repeated Substring) bulan bir algoritma yazın. Bu problem genomlardaki tekrar elementlerini (Repeat Elements) bulmanın temelidir.</p><br/><p><b>Girdi:</b> <code>dna = 'ATGCGTATGCTAA'</code></p><p><b>Beklenen Çıktı:</b> <code>ATGC</code> (ATGC dizisi 1. ve 7. indekslerde tekrar ediyor)</p>",
        "starter_code": "dna = 'ATGCGTATGCTAA';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGCGTATGCTAA';\nen_uzun = '';\nuzunluk = length(dna);\n\n% En uzun alt dizi uzunluğundan geriye doğru arama yapıyoruz\nfor L = floor(uzunluk/2):-1:1\n    for i = 1:uzunluk - L + 1\n        parca = dna(i:i+L-1);\n        % Kalan kısımda bu parça var mı (Örtüşmemesi için i+L'den sonrasına bakılır)\n        kalan_dizi = dna(i+L:end);\n        if contains(kalan_dizi, parca)\n            en_uzun = parca;\n            break; % Parçayı bulduk, bu L uzunluğu için en uzunu budur\n        end\n    end\n    if ~isempty(en_uzun)\n        break; % En uzun parçayı bulduğumuz için dış döngüyü de kırıyoruz\n    end\nend\n\ndisp(en_uzun);",
        "expected_output": "ATGC",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Tandem Tekrarları ve Transpozonlar)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>İnsan genomunun yarısından fazlası proteini kodlamayan, sadece kendini tekrar eden dizilerden (Repetitive Elements) oluşur. Bu tekrarlar ya yan yana bitişik (Tandem Repeats - örneğin telomer bölgesindeki TTAGGG tekrarları) ya da genomun farklı yerlerine dağılmış (Interspersed Repeats - örneğin Alu elementleri veya transpozonlar denilen sıçrayan genler) olabilir. Bir dizinin kendi içindeki tekrar eden en uzun parçasını bulmak, veri sıkıştırma algoritmaları için önemli olduğu kadar, genetik hastalıklara neden olabilen tekrar genişlemelerini (Repeat Expansion) analiz etmek için de kritik bir işlemdir. Biyoinformatik literatüründe bu, En Uzun Ortak Alt Dizi (Longest Common Substring) probleminin farklı bir varyasyonudur.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Verilen dizinin içerisinde, hem kendisi bir yerde var olan hem de kendisinden bağımsız (örtüşmeyen/non-overlapping) başka bir bölgede tamamen aynısı bulunan dizileri aramalıyız. Bunların içinden en uzun olanını bulmak istiyoruz. Örtüşmemesi çok önemlidir; örneğin 'AAAA' dizisinde 'AAA' tekrar ediyor gibi görünebilir ancak ikinci 'AAA' birincinin içine girmiştir. En az iki parçaya ihtiyacımız olduğu için teorik olarak bulunabilecek maksimum tekrar uzunluğu, dizinin toplam uzunluğunun yarısıdır (<code>uzunluk / 2</code>).</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemin kaba kuvvet (Brute-force) çözümü oldukça maliyetlidir (O(N^3)). Ancak algoritmayı zekice kurarak hızı artırabiliriz. Aramaya en küçük (1 harflik) tekrarlardan başlamak yerine, <strong>aranabilecek en büyük uzunluktan geriye doğru</strong> (örneğin 6, 5, 4...) sayarak arama yaparız. Böylece bir tekrar bulduğumuz an, bunun matematiksel olarak var olabilecek en uzun tekrar olduğunu biliriz ve tüm döngüleri <code>break</code> komutuyla anında kırarak (kısa devre yaparak) çok büyük bir zaman tasarrufu sağlarız.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'ın yeni sürümlerinde metin arama işlemleri için <code>contains(metin, aranacak_parca)</code> fonksiyonu gelmiştir. <code>strfind</code> bize pozisyon (indeks) verirken, <code>contains</code> sadece hızlı bir mantıksal Doğru/Yanlış (true/false) döndürür ve koşullu ifadeler (if-else) için çok daha okunabilir ve hızlı bir seçenektir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>for L = floor(uzunluk/2):-1:1</code> : Olası tekrar uzunluğunu (L) temsil eden dış döngümüzü kuruyoruz. Dizinin yarısından başlıyor ve 1'er 1'er eksilerek (<code>:-1</code>) 1'e kadar iniyor. En uzun olasılıktan başlamak optimizasyonun sırrıdır.</li>
        <li><code>for i = 1:uzunluk - L + 1</code> : Kayan pencere iç döngümüzü başlatıyoruz.</li>
        <li><code>parca = dna(i:i+L-1);</code> : L uzunluğundaki alt diziyi (slice) kesip çıkarıyoruz.</li>
        <li><code>kalan_dizi = dna(i+L:end);</code> : Örtüşmeyi engellemek (non-overlapping) için, dizinin geri kalanını (parçanın bittiği noktanın bir sağından dizinin sonuna kadar olan kısmı) alıyoruz.</li>
        <li><code>if contains(kalan_dizi, parca)</code> : MATLAB'ın yerleşik arama fonksiyonu ile, aldığımız parçanın \"kalan_dizi\" içinde geçip geçmediğini kontrol ediyoruz.</li>
        <li><code>en_uzun = parca; break;</code> : Eğer geçiyorsa (bulunduysa), aradığımız cevap kesinlikle budur çünkü aramaya en uzundan başlamıştık. Parçayı kaydedip iç döngüyü <code>break</code> ile kırıyoruz.</li>
        <li><code>if ~isempty(en_uzun) break; end</code> : İç döngü kırıldıktan sonra sonuç bulunduysa, gereksiz yere daha küçük uzunlukları (L-1, L-2...) aramaması için dış döngüyü de kırıp işlemi bitiriyoruz. Sonuç yazdırılıyor.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i10", "level": "intermediate",
        "title": "10. Rastgele Mutasyon Simülasyonu (Monte Carlo Temelleri)",
        "description": "<p>Bir DNA dizisi ve bir mutasyon olasılığı (örn: P = 0.1, %10 ihtimal) verildiğinde, her bir nükleotidin üzerinden geçerek %10 ihtimalle o nükleotidi rastgele başka bir nükleotid (A,C,G,T) ile değiştiren bir simülasyon kodu yazın.</p><br/><p><b>Girdi:</b> <code>dna='AAAAAAAAAA', mut_orani=0.1</code></p><p><b>Beklenen Çıktı:</b> <code>AATAACAAAA</code> (Girdi dizisine benzeyen ancak birkaç harfi değişmiş, tamamen rastgele üretilmiş bir çıktı)</p>",
        "starter_code": "dna = 'AAAAAAAAAA';\nmutasyon_orani = 0.1;\nbazlar = ['A', 'C', 'G', 'T'];\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'AAAAAAAAAA';\nmutasyon_orani = 0.1;\nbazlar = ['A', 'C', 'G', 'T'];\nmutant_dna = dna;\n\n% Tekrarlanabilirlik için seed ayarlanabilir (opsiyonel)\n% rng('default');\n\nfor i = 1:length(dna)\n    % 0 ile 1 arasında rastgele bir sayı üretiyoruz\n    rastgele_sayi = rand();\n    \n    % Eğer sayı mutasyon oranından küçükse mutasyon gerçekleşir\n    if rastgele_sayi < mutasyon_orani\n        % 1 ile 4 arasında rastgele tam sayı (indeks) seç\n        rastgele_indeks = randi(4);\n        mutant_dna(i) = bazlar(rastgele_indeks);\n    end\nend\ndisp(mutant_dna);",
        "expected_output": "(Rastgelelik içerir. Örn: AATAAAAAGA)",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Rastgele Mutasyon ve Evrim Modelleri)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Doğada DNA polimeraz enzimi yeni bir DNA ipliği sentezlerken son derece güvenilirdir ancak hata oranı sıfır değildir (genellikle 10 milyar bazda bir hata yapar). UV radyasyonu veya kimyasal mutajenler gibi dış faktörler bu hata oranını artırır. Evrimsel biyologlar, popülasyon genetiği modellerini test etmek için nesiller boyunca sürecek mutasyonları bilgisayar ortamında simüle ederler (İleri yönlü simülasyon - Forward Simulation). Bu tür olasılıksal simülasyonların temeli <strong>Monte Carlo</strong> yaklaşımıdır.</p>
        <p>Her bir nükleotidin belirli bir frekansla rastgele başka bir nükleotide dönüşmesi simüle edilir. Jukes-Cantor gibi evrimsel modellerde bu mutasyon ihtimali A, C, G ve T için eşitken, Kimura modelinde transisyon ve transversiyon ihtimalleri birbirinden ayrılır. Biz bu problemde Jukes-Cantor tarzı eş-olasılıklı (equiprobable) basit bir Monte Carlo simülasyonu kuracağız.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Elimizde bir dizi ve %10'u (0.1) temsil eden bir olasılık (P) değeri var. Algoritmamız dizinin ilk harfinden son harfine doğru adım adım ilerlemelidir. Her bir harfe geldiğinde bir zar atmalı (0 ile 1 arasında rastgele bir sayı çekmeli). Eğer bu çekilen zar 0.1'den küçükse (yani %10'luk mutasyon ihtimaline denk geldiyse), o pozisyondaki orijinal harfi silmeli ve A, C, G, T harflerinden oluşan bir havuzdan kapalı gözle çektiği rastgele yeni bir harfi oraya atamalıdır. Eğer zar 0.1'den büyük çıkarsa harfe dokunmadan yoluna devam etmelidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB rastgele sayı üretimi konusunda çok güçlü yerleşik fonksiyonlara sahiptir. <code>rand()</code> fonksiyonu, matematikteki Düzgün Dağılıma (Uniform Distribution) göre 0.000 ile 1.000 arasında ondalıklı bir sayı üretir. Bu fonksiyon olasılık eşiğini (P=0.1) aşmak için kullanılır. Diğer yandan, A, C, G, T arasından birini seçmek için ondalıklı değil 1, 2, 3 veya 4 gibi bir tam sayıya ihtiyacımız vardır. Bunun için de rastgele tam sayı (Random Integer) üreten <code>randi(4)</code> fonksiyonu kullanılır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Rastgele (Random) çalışan algoritmaları kodlarken en büyük sorun kodun düzgün çalışıp çalışmadığını test edememektir, çünkü her seferinde farklı sonuç verir. Hata ayıklama (Debugging) sırasında kodun başına <code>rng('default')</code> (Random Number Generator Seed) komutunu eklerseniz, MATLAB'ın içsel saati sıfırlanır ve rastgele fonksiyonu her çalıştırdığınızda tamamen aynı \"rastgele\" sayı dizisini üretir. Gerçek kullanıma sunulacağı zaman bu satır silinir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>bazlar = ['A', 'C', 'G', 'T'];</code> : Mutasyon gerçekleştiğinde içinden yeni bir harf seçeceğimiz torbamızı (vektörü) hazırlıyoruz.</li>
        <li><code>mutant_dna = dna;</code> : Orijinal diziyi korumak için simülasyonu çalıştıracağımız bir kopyasını alıyoruz.</li>
        <li><code>for i = 1:length(dna)</code> : Diziyi baştan sona tarayan döngüyü kuruyoruz.</li>
        <li><code>rastgele_sayi = rand();</code> : 0 ile 1 arasında ondalıklı bir zar atıyoruz (örn: 0.452 veya 0.089).</li>
        <li><code>if rastgele_sayi < mutasyon_orani</code> : Atılan zar, eşik değerimizden (0.1) küçükse bloğa giriyoruz. (%10 ihtimal)</li>
        <li><code>rastgele_indeks = randi(4);</code> : 1, 2, 3 veya 4 sayılarından birini rastgele çekiyoruz. (Örn: 2)</li>
        <li><code>mutant_dna(i) = bazlar(rastgele_indeks);</code> : Çektiğimiz sayıyı baz vektörümüzün indeksi olarak kullanıyoruz (örn: bazlar(2) bize 'C'yi verir) ve mutasyon geçirecek i. pozisyona bu yeni harfi yazıyoruz.</li>
        <li>Sonuç olarak yapısı bozulmuş (mutasyonlu) yeni DNA'yı ekrana yazdırıyoruz.</li>
    </ul>
</div>
        """
    }
]

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
