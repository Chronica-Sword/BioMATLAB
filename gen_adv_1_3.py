# coding: utf-8
import json

with open("data.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("const problems = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

problems = json.loads(json_str)

adv_data = [
    {
        "id": "a1", "level": "advanced",
        "title": "1. Needleman-Wunsch Global Hizalama Matrisi (Tam Çözüm)",
        "description": "<p>Needleman-Wunsch algoritmasının en kritik bölümü olan Matris Doldurma (Matrix Fill) aşamasını kodlayın. İki DNA dizisini alın, boşluk (gap = -2), eşleşme (match = 1) ve eşleşmeme (mismatch = -1) kurallarına göre (M+1)x(N+1) boyutundaki tüm Dinamik Programlama skor matrisini hesaplayıp ekrana yazdırın.</p><br/><p><b>Girdi:</b> <code>seq1='GATT', seq2='GCAT'</code></p><p><b>Beklenen Çıktı:</b> 5x5 boyutlarında, sağ alt köşesinde maksimum hizalama skoru (2) bulunan tam dolu Dinamik Programlama Matrisi.</p>",
        "starter_code": "seq1 = 'GATT';\nseq2 = 'GCAT';\nmatch = 1; mismatch = -1; gap = -2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "seq1 = 'GATT';\nseq2 = 'GCAT';\nmatch = 1; mismatch = -1; gap = -2;\n\nm = length(seq1);\nn = length(seq2);\n\n% 1. İlklendirme (Initialization)\nskor_matrisi = zeros(m + 1, n + 1);\nfor i = 2:m+1\n    skor_matrisi(i, 1) = skor_matrisi(i-1, 1) + gap;\nend\nfor j = 2:n+1\n    skor_matrisi(1, j) = skor_matrisi(1, j-1) + gap;\nend\n\n% 2. Matris Doldurma (Matrix Fill)\nfor i = 2:m+1\n    for j = 2:n+1\n        % Harfler eşleşiyor mu?\n        if seq1(i-1) == seq2(j-1)\n            s = match;\n        else\n            s = mismatch;\n        end\n        \n        % 3 Farklı Yoldan Gelebilecek Skorları Hesapla\n        yol_capraz = skor_matrisi(i-1, j-1) + s;\n        yol_ust    = skor_matrisi(i-1, j) + gap;\n        yol_sol    = skor_matrisi(i, j-1) + gap;\n        \n        % En yüksek (maksimum) puanı seç ve hücreye yaz\n        skor_matrisi(i, j) = max([yol_capraz, yol_ust, yol_sol]);\n    end\nend\n\ndisp('Hesaplanan Dinamik Programlama Matrisi:');\ndisp(skor_matrisi);",
        "expected_output": "Hesaplanan Dinamik Programlama Matrisi:\n     0    -2    -4    -6    -8\n    -2     1    -1    -3    -5\n    -4    -1     0    -2    -4\n    -6    -3    -2     1    -1\n    -8    -5    -4    -1     2",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Evrimsel Homoloji ve Dinamik Programlama)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyolojinin en derin ve temel prensiplerinden biri, evrimsel süreçte yapıların (ve dolayısıyla bu yapıları kodlayan dizilerin) korunmasıdır. Farklı türlerdeki proteinlerin veya genlerin aynı temel işleve (fonksiyona) sahip olup olmadığını anlamanın yegane yolu, onların DNA dizilimlerini alt alta koyarak (Hizalama - Alignment) ne kadar benzediklerine bakmaktır. Eğer iki dizi %30'dan fazla birbirine benziyorsa (Homoloji), bu dizilerin milyonlarca yıl önce ortak bir atadan türediği ve benzer işlevlere sahip olduğu varsayılır. Ancak mutasyonlar (harf değişimi) ve delesyon/insersiyonlar (harf kayıpları ve kazanımları, yani boşluklar) nedeniyle iki diziyi mükemmel şekilde alt alta oturtmak basit bir kaydırma işlemi ile yapılamaz.</p>
        <p>İki dizi arasındaki olası tüm hizalama kombinasyonlarının sayısı astronomiktir. Örneğin, 100 harflik iki dizinin olası hizalama şekli evrendeki atom sayısına yaklaşır. Bu devasa problemi çözmek için 1970 yılında Saul Needleman ve Christian Wunsch, bilgisayar bilimlerinin \"Dinamik Programlama (Dynamic Programming)\" tekniğini biyolojiye uyarladılar. Dinamik programlama, devasa bir problemi küçük alt problemlere (harf harf eşleşmelere) böler, bu alt problemlerin en iyi çözümünü bir matrisin (tablonun) hücrelerine kaydeder (Memoization) ve problem büyüdükçe geçmişte hesaplanmış en iyi yolları kullanarak nihai sonuca ulaşır. Bu algoritma, tüm biyoinformatik endüstrisinin üzerine inşa edildiği temel taştır ve iki diziyi başından sonuna kadar uç uca hizalamayı garanti eder (Global Alignment).</p>
        <p>Algoritmanın biyolojik felsefesi oldukça basittir: Doğada iki harfin aynı kalması (Match) evrimsel bir başarıdır ve ödüllendirilmelidir (+1 puan). Bir harfin başka bir harfe mutasyona uğraması (Mismatch) küçük bir kusurdur ve hafif cezalandırılmalıdır (-1 puan). Ancak dizinin ortasına yeni bir harf girmesi veya bir harfin silinmesi (Indel mutasyonları), okuma çerçevesini bozabileceği için çok daha ağır bir mutasyondur ve buna karşılık gelen boşluk eklemeleri (Gap) ağır cezalandırılmalıdır (-2 puan). Algoritmanın amacı, toplam puanı maksimize eden (en az mutasyon gerektiren) evrimsel yolu bulmaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız, Orta Seviyede \"Matris İlklendirme\" olarak temelini attığımız Needleman-Wunsch matrisinin iç kısımlarını tamamen doldurmaktır. Girdi olarak <code>seq1</code> (boyutu M) ve <code>seq2</code> (boyutu N) alınır. Toplam boyutu <code>(M+1) x (N+1)</code> olan bir ızgara (grid) oluşturulur. Ekstra satır ve sütun, 0. indeks (hizalamanın başlamadığı boş uzay) içindir. Matrisin ilk satırı ve ilk sütunu boşluk cezaları ile (0, -2, -4, -6...) doldurulduktan sonra, geriye kalan her bir boş hücre için üç farklı yol (çaprazdan gelmek, üstten gelmek, soldan gelmek) hesaplanmalı ve bu üç yoldan matematiksel olarak <strong>en büyük</strong> (en avantajlı) olanı seçilip hücreye yazılmalıdır. Matrisin sağ alt köşesinde oluşan rakam, bu iki dizinin olası tüm evrimsel kombinasyonları içindeki maksimum hizalama skorudur.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB gibi matris tabanlı dillerde, iç içe geçmiş For döngüleri (Nested Loops) genellikle yavaş çalışır ve kodlayıcılar her zaman döngüleri vektörize etmeye çalışırlar. Ancak Dinamik Programlamada bir hücrenin (i, j) hesaplanabilmesi için, solundaki (i, j-1), üstündeki (i-1, j) ve sol üst çaprazındaki (i-1, j-1) hücrelerin önceden kesinlikle hesaplanmış olması şarttır. Bu katı bağımlılık (Data Dependency) nedeniyle, Needleman-Wunsch matris doldurma işlemi basitçe vektörize edilemez; geleneksel olarak satır satır veya sütun sütun döngülerle işlenmek zorundadır (Anti-diagonal wavefront optimizasyonları gibi ileri C++ teknikleri hariç).</p>
        <p>Kodumuzda performansı korumanın en önemli yolu, dizi indekslemesinde boyut kaymalarına dikkat etmektir. Matrisimiz <code>(M+1) x (N+1)</code> boyutundadır ve 1. indeksler boşlukları temsil eder. Bu nedenle ana harfleri karşılaştırırken, matristeki (i, j) hücresi, gerçek DNA dizisindeki (i-1, j-1) indekslerine karşılık gelir. Eğer bu kaydırmayı unutursanız, algoritma tamamen yanlış harfleri karşılaştırarak anlamsız bir skor tablosu üretecektir. Üç yolu hesaplarken MATLAB'ın <code>max([A, B, C])</code> fonksiyonu, kodu if-else yığınından kurtaran son derece temiz ve yerleşik bir fonksiyondur.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>m = length(seq1); n = length(seq2);</code> : Dizilerin boyları çıkarılır.</li>
        <li><code>skor_matrisi = zeros(m + 1, n + 1);</code> : 0. indeksleri temsil edecek ekstra bir sınır (padding) bırakılarak, bellekte matrisin çerçevesi oluşturulur ve sıfırlarla ön tahsis (pre-allocation) yapılır.</li>
        <li><strong>İlklendirme Döngüleri:</strong> <code>skor_matrisi(i, 1) = skor_matrisi(i-1, 1) + gap;</code> mantığıyla ilk sütun (-2, -4, -6...) aşağı doğru ve ilk satır sağa doğru (-2, -4, -6...) doldurulur. Bu, dizilerden birinin sadece boşluklardan (deletion) oluştuğu senaryonun skorudur.</li>
        <li><code>for i = 2:m+1</code> ve <code>for j = 2:n+1</code> : Matrisin içi satır satır ve soldan sağa taranmaya başlanır. (İndekslerin 2'den başlamasının nedeni, 1. satır ve sütunun ilklendirilmiş olmasıdır).</li>
        <li><code>if seq1(i-1) == seq2(j-1)</code> : Matristeki (i,j) koordinatı için dizilerdeki ilgili harfler çekilir. Eğer harfler aynıysa <code>s</code> (geçici skor) değişkeni 1 (Match) olur, değilse -1 (Mismatch) olur.</li>
        <li><strong>yol_capraz = skor_matrisi(i-1, j-1) + s;</strong> : Biyolojik anlamı: Her iki diziden de birer harf aldık (okuma çerçevesini bozmadık), ya eşleştik ya da mutasyon var. Çaprazdaki eski toplam skora <code>s</code> eklenir.</li>
        <li><strong>yol_ust = skor_matrisi(i-1, j) + gap;</strong> : Biyolojik anlamı: 1. diziden bir harf aldık ama 2. dizinin karşısına boşluk (-) koyduk. Üst komşunun skoruna -2 eklenir.</li>
        <li><strong>yol_sol = skor_matrisi(i, j-1) + gap;</strong> : Biyolojik anlamı: 2. diziden harf aldık, 1. dizinin karşısına boşluk (-) koyduk. Sol komşunun skoruna -2 eklenir.</li>
        <li><code>skor_matrisi(i, j) = max([yol_capraz, yol_ust, yol_sol]);</code> : Bu 3 olası evrimsel senaryodan hangisi bize matematiksel olarak en yüksek skoru sağlıyorsa, hücrenin nihai değeri olarak o seçilir. Dinamik programlamanın \"Geçmiş kararların en iyisini seç\" (Optimal Substructure) kuralı burada işletilir.</li>
        <li>Döngü bittiğinde <code>disp(skor_matrisi)</code> ile tam matris basılır. En sağ alt hücre (m+1, n+1), bu iki gen dizisinin ulaşabileceği nihai benzerlik skorudur.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a2", "level": "advanced",
        "title": "2. UPGMA Filogenetik Uzaklık (Mesafe) Matrisi Çıkarma",
        "description": "<p>Evrimsel akrabalık ağaçları (Filogenetik Ağaçlar) oluştururken UPGMA algoritması kullanılır. Bu algoritmanın ilk adımı, verilen tüm türlerin (DNA dizilerinin) birbirleriyle olan genetik uzaklıklarını (Farklı nükleotid sayısı / Toplam uzunluk) içeren çapraz bir Uzaklık Matrisi (Distance Matrix) oluşturmaktır. N adet eşit uzunlukta dizi için NxN boyutunda simetrik bir matris oluşturan kodu yazın.</p><br/><p><b>Girdi:</b> <code>T1='ATGC', T2='ATCC', T3='TTCA'</code> (T: Tür)</p><p><b>Beklenen Çıktı:</b><br/>0.00  0.25  0.75<br/>0.25  0.00  0.50<br/>0.75  0.50  0.00</p>",
        "starter_code": "% Türlerin genetik dizileri (Hepsi eşit uzunlukta)\nturler = {'ATGC', 'ATCC', 'TTCA'};\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "turler = {'ATGC', 'ATCC', 'TTCA'};\nn = length(turler);\nuzunluk = length(turler{1});\n\n% NxN boyutunda boş bir uzaklık matrisi oluşturuyoruz\nuzaklik_matrisi = zeros(n, n);\n\n% Tüm türleri birbirleriyle karşılaştırıyoruz\nfor i = 1:n\n    for j = i+1:n % Simetrik olduğu için i+1'den başlatarak zaman kazanıyoruz\n        dizi1 = turler{i};\n        dizi2 = turler{j};\n        \n        % İki dizi arasındaki farkları (Hamming mesafesi) buluyoruz\n        farkli_harf_sayisi = sum(dizi1 ~= dizi2);\n        \n        % P-distance (Oransal uzaklık) hesabı: Fark / Toplam uzunluk\n        p_distance = farkli_harf_sayisi / uzunluk;\n        \n        % Matrise atama (Simetrik olarak iki tarafa da yazıyoruz)\n        uzaklik_matrisi(i, j) = p_distance;\n        uzaklik_matrisi(j, i) = p_distance;\n    end\nend\n\ndisp('UPGMA Uzaklık Matrisi:');\ndisp(uzaklik_matrisi);",
        "expected_output": "UPGMA Uzaklık Matrisi:\n         0    0.2500    0.7500\n    0.2500         0    0.5000\n    0.7500    0.5000         0",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Filogenetik Ağaçlar ve UPGMA Algoritması)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Dünya üzerindeki türlerin (örneğin İnsan, Şempanze, Goril ve Fare) evrimsel olarak birbirlerine ne kadar yakın akraba olduklarını (hangi ortak atadan ne zaman ayrıldıklarını) görselleştirmek için ağaç diyagramları çizilir. Bu diyagramlara <strong>Filogenetik Ağaçlar (Dendrogram)</strong> denir. Darwin'in Türlerin Kökeni kitabındaki meşhur \"I think\" (Sanırım) karalaması, tarihteki ilk filogenetik ağaç çizimidir. Günümüzde bu ağaçlar, canlıların fiziksel görünüşlerine göre değil, genetik kodlarına (DNA) bakılarak muazzam bir matematiksel kesinlikle çizilir.</p>
        <p>DNA verisinden filogenetik ağaç oluşturmanın birçok yöntemi vardır (Maximum Likelihood, Neighbor-Joining vb.). Bunlardan kavramsal olarak en anlaşılır ve tarihsel olarak en önemlilerinden biri <strong>UPGMA (Unweighted Pair Group Method with Arithmetic Mean)</strong> algoritmasıdır. UPGMA bir \"Hiyerarşik Kümeleme (Clustering)\" algoritmasıdır. Algoritma çalışmaya başlamadan önce, elimizdeki tüm türlerin genetik dizilerinin birbirleriyle olan \"Mesafelerini\" (Uzaklıklarını) bilmek zorundadır. Mesafe demek, biyolojide iki dizinin birbirinden ne kadar farklı olduğu demektir. İki dizi birbirinin tamamen aynısıysa mesafe 0'dır. Tamamen farklılarsa mesafe 1'dir. Evrimsel moleküler saat (Molecular Clock) hipotezine göre, mutasyonlar sabit bir hızda birikir. Dolayısıyla iki tür arasındaki genetik mesafe ne kadar fazlaysa, evrim ağacında birbirlerinden o kadar uzun zaman önce ayrılmışlar (uzak akraba olmuşlar) demektir. UPGMA algoritması bu uzaklık matrisine bakar, matristeki en küçük sayıyı (en yakın iki akrabayı) bulur ve onları ağaçta birleştirerek tek bir dal (küme) haline getirir. Daha sonra matrisi günceller ve ağacın köküne ulaşana kadar bu işlemi tekrar eder. Bu problemde, ağaç çizimi için hayati öneme sahip olan ilk adımı, yani <strong>Uzaklık Matrisini (Distance Matrix)</strong> oluşturacağız.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize N adet farklı türün eşit uzunluktaki DNA dizileri bir hücre dizisi (Cell array) içinde verilmiştir (Bu problemde N=3). Amacımız NxN boyutunda iki boyutlu bir matris oluşturmaktır. Bu matrisin satırları ve sütunları türleri temsil eder (1. satır Tür 1, 2. sütun Tür 2 gibi). Bir hücredeki (i,j) değer, i. tür ile j. tür arasındaki P-Distance (Oransal Uzaklık) değeridir. P-distance, iki dizideki farklı karakter sayısının, dizinin toplam uzunluğuna bölünmesiyle bulunur. Türlerin kendileriyle olan uzaklıkları elbette sıfır olmalıdır (Matrisin ana köşegeni (diagonal) tamamen sıfırlardan oluşmalıdır).</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Tüm türleri birbirleriyle kıyaslamak için iç içe geçmiş iki for döngüsüne (<code>i</code> ve <code>j</code>) ihtiyacımız var. Ancak burada çok ciddi bir algoritmik optimizasyon fırsatı vardır. Tür 1 ile Tür 2 arasındaki uzaklık (örneğin 0.25), matematiksel ve biyolojik olarak Tür 2 ile Tür 1 arasındaki uzaklığa eşittir. Bu, elde edeceğimiz matrisin <strong>Simetrik Matris</strong> olacağı anlamına gelir. Eğer iç döngüyü (<code>j</code>) her seferinde 1'den başlatırsak, hem Tür 1-Tür 2'yi hesaplar, hem de gereksiz yere Tür 2-Tür 1'i tekrar hesaplar (Yüzlerce tür olduğunda işlem süresi iki katına çıkar). Bunun yerine iç döngüyü <code>j = i+1</code>'den başlatırsak, sadece matrisin üst üçgenini (Upper Triangle) hesaplarız. Alt üçgene ise üstte bulduğumuz değeri kopyalarız (<code>matris(j,i) = matris(i,j)</code>). Bu optimizasyon, O(N^2) karmaşıklığını O(N^2 / 2) seviyesine indirerek işlem süresini yarı yarıya azaltır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da hücre dizilerindeki (Cell Arrays) gerçek karakter verisine ulaşmak için süslü parantez <code>{}</code> kullanmak zorunludur. Eğer <code>turler(1)</code> yazarsanız size 'ATGC' metnini değil, içinde 'ATGC' olan bir paket/kutu döndürür ve matematiksel vektör karşılaştırması (<code>~=</code>) yapamazsınız. Her zaman <code>turler{1}</code> şeklinde hücrenin içini boşaltmalısınız.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>n = length(turler);</code> : Elimizde kaç adet tür olduğunu (N boyutunu) buluyoruz. Bu problemde 3.</li>
        <li><code>uzunluk = length(turler{1});</code> : Dizilerin nükleotid uzunluklarını (L) buluyoruz. Tüm türler eşit uzunlukta olduğu için (Örn: 4 harf), sadece 1. türün uzunluğuna bakmak yeterlidir.</li>
        <li><code>uzaklik_matrisi = zeros(n, n);</code> : NxN boyutunda, yani 3x3 bir matris oluşturup içini sıfırlarla dolduruyoruz (Pre-allocation). Bu sayede Tür 1-Tür 1 (diagonal) eşleşmeleri otomatik olarak 0 kalmış olur.</li>
        <li><strong>Dış Döngü:</strong> <code>for i = 1:n</code> : Kıyaslanacak baz türü (Reference) seçer.</li>
        <li><strong>İç Döngü (Optimizasyonlu):</strong> <code>for j = i+1:n</code> : Karşılaştırılacak hedef türü seçer. <code>i+1</code>'den başlaması sayesinde kendisiyle (i=j) ve daha önce hesaplanmış geride kalan türlerle karşılaştırma yapılmaz.</li>
        <li><code>farkli_harf_sayisi = sum(dizi1 ~= dizi2);</code> : Vektörel karşılaştırma. İki diziyi üst üste koyar, harflerin eşit olmadığı (mutasyon olan) indeksleri bulup (1 yapar) toplar. Bu bize mutlak \"Hamming Mesafesi\"ni verir.</li>
        <li><code>p_distance = farkli_harf_sayisi / uzunluk;</code> : Hamming mesafesini dizinin uzunluğuna bölerek oransal P-Distance metriğini elde ederiz. (Örn: 1 farklı harf / 4 toplam uzunluk = 0.25).</li>
        <li><strong>Simetrik Atama:</strong> <code>uzaklik_matrisi(i, j) = p_distance;</code> ile matrisin üst üçgenine değeri yazarız. <code>uzaklik_matrisi(j, i) = p_distance;</code> ile aynı değeri aynadan yansıtarak alt üçgene yazarız.</li>
        <li>Döngü bittiğinde elde edilen evrimsel mesafe matrisi ekrana yazdırılır. UPGMA algoritması bu matrisi alarak en küçük sayıdan dallandırmaya başlayacaktır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a3", "level": "advanced",
        "title": "3. Saklı Markov Modelleri (HMM): Viterbi Kod Çözücüsü (Basit CpG Adası)",
        "description": "<p>Bir DNA dizisinde, her harfin normal bir bölgeden (Normal State) mi yoksa bir CpG Adacığı bölgesinden (Island State) mi geldiğini tahmin etmek için çok basit bir Hidden Markov Model (HMM) - Viterbi Algoritması yazın. <br/>Normal bölgede (N) C ve G görme ihtimali düşüktür. Island bölgesinde (I) C ve G görme ihtimali yüksektir. Viterbi algoritması, gözlemlenen harflere bakarak en olası durumu (N veya I) matematiksel olarak tahmin eder.</p><br/><p><b>Girdi:</b> <code>dna='ATCG'</code> (Geçiş ve Emisyon olasılıkları kod içinde verilecek)</p><p><b>Beklenen Çıktı:</b> <code>NNII</code> (A ve T normal bölgeyi, C ve G ise CpG adası bölgesini işaret eder)</p>",
        "starter_code": "dna = 'ATCG';\n% Algoritma karmaşık olduğu için başlangıç taslağı\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATCG';\n\n% 1. Emisyon (Yayınım) Olasılıkları (Hangi durumda hangi harf ne kadar olası?)\n% Normal Durum (N) için: A ve T yüksek (%40), C ve G düşük (%10)\np_emit_N = containers.Map({'A','C','G','T'}, [0.4, 0.1, 0.1, 0.4]);\n\n% Island Durumu (I) için: C ve G yüksek (%40), A ve T düşük (%10)\np_emit_I = containers.Map({'A','C','G','T'}, [0.1, 0.4, 0.4, 0.1]);\n\n% 2. Geçiş (Transition) Olasılıkları (Durumlar arası geçiş ne kadar olası?)\np_trans_NN = 0.8; % Normalden Normale kalma %80\np_trans_NI = 0.2; % Normalden Island'a geçiş %20\np_trans_II = 0.8; % Island'da kalma %80\np_trans_IN = 0.2; % Island'dan Normale dönüş %20\n\n% Dinamik Programlama Matrisleri\nviterbi_N = zeros(1, length(dna)); % Normal durum skorları\nviterbi_I = zeros(1, length(dna)); % Island durum skorları\ngeri_izleme = zeros(1, length(dna)); % 1: N'den geldi, 2: I'dan geldi\n\n% Başlangıç durumu (İlk harf için %50-%50 eşit ihtimal varsayıyoruz)\nviterbi_N(1) = 0.5 * p_emit_N(dna(1));\nviterbi_I(1) = 0.5 * p_emit_I(dna(1));\n\n% Viterbi Matrisini Doldurma\nfor t = 2:length(dna)\n    harf = dna(t);\n    \n    % O anki harfin N olma ihtimalini hesapla (İki yoldan hangisi daha iyi?)\n    yol1_NN = viterbi_N(t-1) * p_trans_NN * p_emit_N(harf);\n    yol2_IN = viterbi_I(t-1) * p_trans_IN * p_emit_N(harf);\n    \n    if yol1_NN > yol2_IN\n        viterbi_N(t) = yol1_NN;\n        yol_N = 1; % N'den geldi\n    else\n        viterbi_N(t) = yol2_IN;\n        yol_N = 2; % I'dan geldi\n    end\n    \n    % O anki harfin I olma ihtimalini hesapla\n    yol3_NI = viterbi_N(t-1) * p_trans_NI * p_emit_I(harf);\n    yol4_II = viterbi_I(t-1) * p_trans_II * p_emit_I(harf);\n    \n    if yol4_II > yol3_NI\n        viterbi_I(t) = yol4_II;\n        yol_I = 2; % I'dan geldi\n    else\n        viterbi_I(t) = yol3_NI;\n        yol_I = 1; % N'den geldi\n    end\nend\n\n% Geri İzleme (Traceback) - En muhtemel dizilimi (State Sequence) bulma\ndurum_dizisi = blanks(length(dna));\nif viterbi_N(end) > viterbi_I(end)\n    durum_dizisi(end) = 'N';\nelse\n    durum_dizisi(end) = 'I';\nend\n\n% Basitleştirilmiş görsel atama (Bu versiyonda anlık skora göre karar veriyoruz)\nfor t = 1:length(dna)\n    if viterbi_N(t) > viterbi_I(t)\n        durum_dizisi(t) = 'N';\n    else\n        durum_dizisi(t) = 'I';\n    end\nend\n\ndisp('Tahmin Edilen Gizli Durumlar (Hidden States):');\ndisp(durum_dizisi);",
        "expected_output": "Tahmin Edilen Gizli Durumlar (Hidden States):\nNNII",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Gizli Markov Modelleri ve CpG Adacıkları)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte DNA dizisine bakarak \"Burada bir gen başlıyor\", \"Burası bir intron\" veya \"Burada bir CpG metilasyon adacığı var\" gibi tahminler (Annotation) yapmak için yapay zeka algoritmaları kullanılır. Bu alandaki en klasik, istatistiksel olarak en sağlam ve en çok kullanılan algoritma ailesi <strong>Saklı/Gizli Markov Modelleri'dir (Hidden Markov Models - HMM)</strong>. Ünlü gen bulma programları GLIMMER, GENSCAN ve Pfam veritabanı tamamen HMM matematiği üzerine kuruludur.</p>
        <p>HMM'in felsefesi şudur: İki farklı gerçeklik (Durum - State) vardır. Biri görebildiğimiz gerçekliktir (Gözlemlenenler: DNA'daki A,C,G,T harfleri). Diğeri ise bu harfleri üreten ancak bizim dışarıdan göremediğimiz biyolojik \"Gizli Durum\"dur (Hidden State: Acaba bu harf Normal bir DNA bölgesinden mi üretildi, yoksa C ve G açısından çok zengin olan epigenetik bir CpG Adası bölgesinden mi üretildi?). Amacımız, sadece elimizdeki harflere (Gözlemlere) ve önceden bildiğimiz istatistiksel kurallara (Olasılıklara) bakarak, dizideki her bir harfin arka planındaki görünmez gizli durumu (N veya I) tahmin etmektir.</p>
        <p>Bu tahmin için üç olasılık parametresi kullanılır: 1) Başlangıç olasılığı, 2) Emisyon/Yayınım Olasılığı (Eğer Normal bölgedeysem C harfi üretme ihtimalim ne? Eğer Ada bölgesindeysem C üretme ihtimalim ne?), 3) Geçiş Olasılığı (Normal bölgeden çıkıp Ada bölgesine girme ihtimalim ne?). Harflerin teker teker incelenerek bu ihtimallerin birbirleriyle çarpılması ve en muhtemel \"Gizli Durumlar Dizilimini\" (En muhtemel yolu) bulma işlemine <strong>Viterbi Algoritması</strong> denir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Sistem bize <code>'ATCG'</code> şeklinde gözlemlenmiş bir DNA metni veriyor. İki gizli durumumuz var: Normal Bölge (N) ve CpG Adası (I). Kurallarımız açık: N bölgesinde A ve T çıkma ihtimali yüksek, C ve G çıkma ihtimali düşüktür. I bölgesinde tam tersi geçerlidir. Ayrıca bir bölgedeysen (Örn N) orada kalma ihtimalin yüksektir (%80), diğer bölgeye geçme (sınırı atlama) ihtimalin düşüktür (%20). Viterbi algoritmasını (Dinamik programlamayı) kullanarak, <code>'ATCG'</code> kelimesini okurken adım adım ihtimalleri çarparak hesaplamalı ve her bir harfin N mi yoksa I mı olmasının daha yüksek ihtimal olduğunu bulmalıyız. Sonuçta 4 harflik yeni bir gizli durum (örn: <code>'NNII'</code>) zinciri elde etmeliyiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Viterbi algoritması da Needleman-Wunsch gibi Dinamik Programlama (DP) mantığıyla çalışır. Ancak burada ödül veya ceza puanlarını toplamak yerine, 0 ile 1 arasındaki ondalıklı \"Olasılık (Probability)\" rakamlarını birbiriyle durmadan çarparız. Algoritmada iki ayrı DP vektörü tutulur: Biri o anki harfe kadar Normal (N) yolundan gelmenin kümülatif olasılık skoru, diğeri Island (I) yolundan gelmenin skorudur. Her adımda bir önceki skorlar yeni geçiş ve emisyon ihtimalleriyle çarpılır. Daha büyük olan olasılık seçilir ve bir sonraki adıma aktarılır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu (Underflow Riski):</strong> Gerçek biyoinformatik uygulamalarında DNA dizisi 4 harf değil, milyonlarca harf uzunluğundadır. 0 ile 1 arasındaki (örn: 0.2 * 0.4 * 0.1...) sayıları milyonlarca kez birbiriyle çarparsanız, sonuç o kadar küçülür ki bilgisayarın işlemci mimarisi bu sayıyı sıfır (0.000...) kabul eder ve sistem çöker (Buna <strong>Underflow</strong> denir). Bunu önlemek için olasılıkların çarpılması yerine Logaritmaları (Log-probabilities) alınarak toplanır. Ancak bu eğitici basit kod parçasında dizi çok kısa olduğu için doğrudan çarpma işlemi kullanılmıştır.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>p_emit_N = containers.Map(...)</code> : Emisyon (Yayınım) ihtimallerini saklamak için iki adet Sözlük (Hash Map) kuruyoruz. N durumu için A ve T ihtimali 0.4, I durumu için C ve G ihtimali 0.4 olarak biyolojik kural setimizi kodluyoruz.</li>
        <li><code>p_trans_NN = 0.8;</code> : Geçiş (Transition) matrisi parametrelerini tanımlıyoruz. Sistem mevcut durumunda kalmayı sever (%80), durum değiştirmeye dirençlidir (%20).</li>
        <li><code>viterbi_N = zeros(1, length(dna));</code> : N ve I ihtimallerinin zaman (harf sırası) boyunca ilerleyişini kaydedeceğimiz dinamik programlama vektörlerini sıfırlarla oluşturuyoruz.</li>
        <li><strong>Başlangıç Durumu (t=1):</strong> Dizinin ilk harfine bakarız. N olma ihtimali (Başlangıç ihtimali (0.5) * İlk harfin N'den çıkma ihtimali). Aynı hesap I için de yapılıp dizilerin 1. indeksine yazılır.</li>
        <li><strong>Viterbi Döngüsü (t=2'den sona kadar):</strong> İkinci harften itibaren geçmişten gelen kararları kullanırız.</li>
        <li><code>yol1_NN = viterbi_N(t-1) * p_trans_NN * p_emit_N(harf);</code> : Şimdiki harfin N olabilmesi için iki ihtimal vardır. Ya bir önceki harf de N idi (NN geçişi). Bu yolun olasılığı: Geçmişin Skoru x N'den N'ye Geçme İhtimali x N'nin Bu Harfi Üretme İhtimali.</li>
        <li><code>yol2_IN = viterbi_I(t-1) * p_trans_IN * p_emit_N(harf);</code> : Ya da bir önceki harf I idi, sınırı atlayıp N'ye geçtik (IN geçişi). Bu yolun olasılığı aynı mantıkla çarpılarak bulunur.</li>
        <li><code>if yol1_NN > yol2_IN</code> : Bu iki yol (NN ve IN) karşılaştırılır. Hangisinin ihtimali daha büyükse, o anki harfin N olma skoru o kabul edilir (Max fonksiyonu mantığı).</li>
        <li>Aynı blok Şimdiki harfin Island (I) olması senaryosu (NI ve II yolları) için de tekrarlanır.</li>
        <li>Döngü bittikten sonra, harf harf hangi skor (N mi yoksa I mı) daha büyükse o harfin gizli durumu olarak atanır ve ekrana <code>'NNII'</code> dizisi basılır. A ve T harfleri Normal, C ve G harfleri Island olarak kusursuz bir şekilde tahmin edilmiş olur.</li>
    </ul>
</div>
        """
    }
]

updated = False
for new_prob in adv_data:
    for i, p in enumerate(problems):
        if p.get("id") == new_prob["id"]:
            problems[i] = new_prob
            updated = True
            break

js_content = "const problems = " + json.dumps(problems, indent=2, ensure_ascii=False) + ";\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
