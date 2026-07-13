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
        "id": "i16", "level": "intermediate",
        "title": "16. DNA Hash Tablosu (Sözlük) Oluşturma",
        "description": "<p>Bir DNA dizisindeki tüm 2'li k-merleri bulup, MATLAB'ın <code>containers.Map</code> objesini (veya modern dictionary objesini) kullanarak her k-merin dizi içinde kaç kez geçtiğini gösteren bir Hash Tablosu oluşturun.</p><br/><p><b>Girdi:</b> <code>dna='ATGCAT'</code></p><p><b>Beklenen Çıktı:</b> <code>'AT':2, 'TG':1, 'GC':1, 'CA':1</code> (Anahtarlar ve Değerleri)</p>",
        "starter_code": "dna = 'ATGCAT';\nk = 2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGCAT';\nk = 2;\n\n% MATLAB'da Hash Table (Dictionary) nesnesi oluşturuyoruz\nkmer_haritasi = containers.Map('KeyType', 'char', 'ValueType', 'int32');\n\nfor i = 1:length(dna)-k+1\n    kmer = dna(i:i+k-1);\n    \n    % Eğer k-mer haritada zaten varsa, değerini 1 artır\n    if isKey(kmer_haritasi, kmer)\n        kmer_haritasi(kmer) = kmer_haritasi(kmer) + 1;\n    else\n        % Haritada yoksa, yeni bir kayıt olarak 1 değerini ata\n        kmer_haritasi(kmer) = 1;\n    end\nend\n\n% Sonuçları okunaklı yazdırma\nanahtarlar = keys(kmer_haritasi);\ndegerler = values(kmer_haritasi);\nfor i = 1:length(anahtarlar)\n    fprintf('%s : %d\\n', anahtarlar{i}, degerler{i});\nend",
        "expected_output": "AT : 2\nCA : 1\nGC : 1\nTG : 1",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Hash Tabloları ve Hızlı Arama)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>BLAST (Basic Local Alignment Search Tool) dünyadaki en popüler biyoinformatik aracıdır. BLAST'ın sırrı, girdiğiniz uzun gen dizisini doğrudan devasa veritabanlarıyla karakter karakter karşılaştırmamasıdır (Bu binlerce yıl sürerdi). Bunun yerine BLAST, öncelikle veritabanındaki tüm dizileri önceden 11 harflik k-mer'lere (word size) böler ve devasa bir Hash Tablosu (Sözlük) oluşturur. Bir k-mer'in hangi genlerde bulunduğu bir kitap indeksi gibi bu sözlükte saklanır.</p>
        <p>Bilgisayar biliminde Hash Tablosu (Dictionary / Map), bir \"Anahtar\" (Key) ile ona bağlı bir \"Değer\"in (Value) saklandığı veri yapısıdır (Örn: \"Ankara\" -> 06). Anahtarlar benzersiz (unique) olmak zorundadır. Arama işlemi bellekte tam yerinde yapıldığı için hızı O(1) düzeyindedir (Yani milyonlarca eleman bile olsa aramayı anında bulur). K-mer frekansı hesaplamak için if-for döngüleri yerine Hash Tablosu kurmak, ileri biyoinformatik programlamanın (k-mer tabanlı analizlerin) temel şartıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize verilen DNA metninin üzerinden kayan pencere (sliding window) ile geçecek ve 2 harflik parçalar koparacağız. Elimizde boş bir Sözlük olacak. Kopardığımız parçayı sözlüğe soracağız: \"Senin içinde AT diye bir kelime var mı?\". Eğer yoksa sözlüğe ekleyip karşısına frekans olarak 1 yazacağız. Eğer sözlükte o kelime zaten varsa, o zaman onun değerini okuyup (örn: 1) üzerine +1 ekleyerek güncelleyeceğiz. Döngü bittiğinde elde edeceğimiz sözlük, bize dizideki tüm parçaların tam dökümünü vermiş olacak.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Python'daki <code>{}</code> objesi (dictionary) neyse, MATLAB'da bunun karşılığı <code>containers.Map</code> objesidir (MATLAB 2022b sonrasında <code>dictionary()</code> fonksiyonu da eklendi ancak Map eski sürümlerle daha uyumludur). Harita tanımlanırken Anahtar'ın veri tipinin karakter dizisi ('char'), Değer'in veri tipinin ise tam sayı ('int32') olacağı sisteme önceden bildirilir. Sözlüğün içinde bir kelime olup olmadığını anlamak için <code>isKey()</code> fonksiyonu kullanılır. Verileri geri çekerken ise <code>keys()</code> ve <code>values()</code> metotları bize hücre dizileri (cell array) döndürür.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da Map objelerine veri atamak veya okumak için normal indeksleme parantezleri <code>()</code> kullanılır. Yani <code>harita('AT') = 5;</code> sintaksı tamamen geçerlidir. Değerleri ekrana basarken dönen sonuçların hücre dizisi (Cell array) olduğunu unutmayın; hücre elemanına süslü parantez <code>{}</code> ile erişmeniz gerekir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>kmer_haritasi = containers.Map('KeyType', 'char', 'ValueType', 'int32');</code> : Boş bir hash tablosu yaratıyoruz. Anahtarlarımız K-mer metinleri ('AT', 'GC'), Değerlerimiz ise bunların geçiş sayıları (1, 2, 5 vb.) olacak.</li>
        <li><code>for i = 1:length(dna)-k+1</code> : Sınır taşmasını önleyen kayan pencere döngümüzü başlatıyoruz.</li>
        <li><code>kmer = dna(i:i+k-1);</code> : O adımı temsil eden 2 harflik parçayı kopardık.</li>
        <li><code>if isKey(kmer_haritasi, kmer)</code> : Bu çok kritik bir adımdır. Eğer k-mer haritada YOKKEN onu artırmaya çalışırsanız (<code>harita(kmer) + 1</code>) MATLAB çöker, çünkü bilinmeyen bir anahtara matematiksel işlem uygulanamaz. Bu yüzden önce sorguluyoruz.</li>
        <li><code>kmer_haritasi(kmer) = 1;</code> : Eğer kelime sözlükte ilk kez görülüyorsa (else bloğu), onu sözlüğe ekleyip eşittir 1 diyoruz.</li>
        <li>Döngü bittikten sonra haritanın içindeki <code>keys</code> ve <code>values</code> listelerini alıp <code>fprintf</code> ile alt alta ekrana basıyoruz.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i17", "level": "intermediate",
        "title": "17. RNA İkincil Yapı: Saç Tokası (Hairpin) Eşleşme Kontrolü",
        "description": "<p>Bir RNA dizisi kendi üzerine katlanarak ikincil bir yapı (Secondary Structure) oluşturabilir. Uç uca katlandığını varsayarak (dizinin başı ve sonu birbirine doğru kapanır), RNA baz eşleşme kurallarına (A-U ve C-G) göre kaç adet bağ oluştuğunu bulan kodu yazın.</p><br/><p><b>Girdi:</b> <code>rna='AUGG--CCAU'</code> (Orta nokta '-')</p><p><b>Beklenen Çıktı:</b> <code>Eşleşen Bağ Sayısı: 4</code> (A-U, U-A, G-C, G-C eşleşmeleri)</p>",
        "starter_code": "rna = 'AUGGCCAU';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "rna = 'AUGGCCAU';\nbag_sayisi = 0;\nuzunluk = length(rna);\n\n% İki ucu birbirine doğru yaklaştıran döngü\nfor i = 1:floor(uzunluk/2)\n    sol_baz = rna(i);\n    sag_baz = rna(uzunluk - i + 1);\n    \n    % RNA Eşleşme Kuralları (A-U ve C-G)\n    if (sol_baz == 'A' && sag_baz == 'U') || (sol_baz == 'U' && sag_baz == 'A')\n        bag_sayisi = bag_sayisi + 1;\n    elseif (sol_baz == 'C' && sag_baz == 'G') || (sol_baz == 'G' && sag_baz == 'C')\n        bag_sayisi = bag_sayisi + 1;\n    end\nend\n\nfprintf('Eşleşen Bağ Sayısı: %d\\n', bag_sayisi);",
        "expected_output": "Eşleşen Bağ Sayısı: 4",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (RNA İkincil Yapıları)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>DNA her zaman çift sarmallı bir yapıdayken, RNA normalde hücre içinde tek iplikli (Single Stranded) halde bulunur. Ancak doğadaki tüm moleküller düşük enerjili kararlı yapıya ulaşmak ister. Tek iplikli bir RNA, serbest halde sallanmak yerine, kendi dizisi içindeki birbirini tamamlayan (komplementer) bölgelerle eşleşip <strong>katlanmayı</strong> tercih eder. Bu katlanmalara Saç Tokası (Hairpin loop) veya Kök-İlmek (Stem-Loop) yapıları denir.</p>
        <p>RNA'daki bu üç boyutlu katlanmalar tesadüf değildir; taşıyıcı RNA'nın (tRNA) yonca yaprahı (cloverleaf) şeklini almasını sağlayan şey budur. Ayrıca hücrede virüslerin tespit edilmesi ve CRISPR gibi bağışıklık sistemlerinin çalışması, rehber RNA'ların oluşturduğu bu ikincil yapılar sayesinde mümkün olur. RNA'daki eşleşme kuralları A-U (Adenin-Urasil) ve C-G (Sitozin-Guanin) şeklindedir (Bazen G-U sallantılı eşleşmesi - wobble base pair - de görülür ancak bu algoritmada klasik eşleşme baz alınmıştır). Biyoinformatik algoritmaları termodinamik enerji kurallarını uygulayarak RNA'nın uzayda nasıl katlanacağını tahmin etmeye çalışır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız çok basit bir kök-ilmek (Hairpin) tahmini yapmaktır. Molekülün ortadan tam ikiye katlandığını varsayıyoruz. Bu durumda 1. sıradaki harf ile en sondaki harf karşı karşıya gelir. 2. harf ile sondan 2. harf karşı karşıya gelir. Baş ve sondan başlayıp ortada buluşan bir algoritma (Two Pointers) ile karşılıklı gelen nükleotid çiftlerini değerlendirecek ve eğer bunlar biyolojik olarak birbirini tutan kurallara (A-U, C-G) uygunsa kurulan bağ sayısını bir artıracağız.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problem programlama dünyasında İki İşaretçi (Two Pointers) algoritması olarak bilinir. MATLAB'da bunu çözmenin en temiz yolu, dizinin uzunluğunun yarısına kadar ilerleyen bir for döngüsü kurmaktır. Döngünün indeksi (<code>i</code>) dizinin başından ilerlerken, <code>uzunluk - i + 1</code> matematiği sayesinde ikinci işaretçi dizinin en sonundan geriye doğru gelir. Karşılıklı gelen harfleri mantıksal kontrollerle (if-elseif) inceleriz.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Döngü sınırını <code>floor(uzunluk/2)</code> şeklinde ayarlamak (aşağı tam sayıya yuvarlama) son derece kritiktir. Eğer RNA dizisi 9 harfliyse, 5. harf (ortadaki harf) katlanma noktası (Loop'un tepesi) olur ve karşısında eşleşecek bir harf olmaz. Bu nedenle ortadaki yalnız harfi işlemeye çalışarak mantık hatası yapmaktan kaçınmış oluruz.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>bag_sayisi = 0;</code> : Katlanma sonucunda oluşacak başarılı hidrojen bağlarının sayısını tutacak değişken.</li>
        <li><code>for i = 1:floor(uzunluk/2)</code> : Dizinin sadece yarısına kadar (merkeze kadar) ilerliyoruz.</li>
        <li><code>sol_baz = rna(i);</code> : Soldan, yani baş kısımdan merkeze doğru ilerleyen harf.</li>
        <li><code>sag_baz = rna(uzunluk - i + 1);</code> : Sağdan, yani kuyruk kısmından merkeze doğru gelen harf. Örneğin i=1 iken uzunluk(8) - 1 + 1 = 8. (8. indeksi alır).</li>
        <li><code>if (sol_baz == 'A' && sag_baz == 'U') || (sol_baz == 'U' && sag_baz == 'A')</code> : Eğer karşılıklı gelen iki harf A-U veya U-A kombinasyonlarından birini oluşturuyorsa bağ kurulmuştur, sayacı artırırız.</li>
        <li>Aynı kural C-G ve G-C eşleşmeleri için de bir <code>elseif</code> ile uygulanır. A-A veya A-G gibi eşleşmelerde bağ kurulmaz ve atlanır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i18", "level": "intermediate",
        "title": "18. Nokta Matrisi (Dot Plot) Görselleştirme Hazırlığı",
        "description": "<p>İki DNA dizisindeki yerel benzerlikleri görmek için Dot Plot (Nokta Grafiği) mantığı kullanılır. Girdi olarak alınan iki diziyi karşılaştırıp (satır-sütun) harflerin aynı olduğu noktalara '1', farklı olduğu noktalara '0' koyarak 2 boyutlu bir matris oluşturan kodu yazın.</p><br/><p><b>Girdi:</b> <code>x='ATG', y='ATC'</code></p><p><b>Beklenen Çıktı:</b><br/>1 0 0 (A)<br/>0 1 0 (T)<br/>0 0 0 (G)</p>",
        "starter_code": "x = 'ATG';\ny = 'ATC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "x = 'ATG';\ny = 'ATC';\nx_len = length(x);\ny_len = length(y);\n\n% Sonuçları tutacağımız sıfırlarla dolu matris (X satır, Y sütun)\ndot_matris = zeros(x_len, y_len);\n\nfor i = 1:x_len\n    for j = 1:y_len\n        if x(i) == y(j)\n            dot_matris(i, j) = 1;\n        end\n    end\nend\n\ndisp(dot_matris);",
        "expected_output": "     1     0     0\n     0     1     0\n     0     0     0",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Dot Plot Metodu)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte iki dizi arasındaki (veya bir dizinin kendi içindeki) karmaşık yapıları (tekrarlar, ters dönmeler-inversions, delesyonlar) insan gözüyle en hızlı şekilde tespit etmenin yolu <strong>Dot Plot (Nokta Grafiği)</strong> yöntemidir. Dizilerden biri matrisin üst tarafına (X ekseni), diğeri sol tarafına (Y ekseni) yerleştirilir. Diziler arasındaki her bir kombinasyon ızgara (grid) üzerinde karşılaştırılır. Eğer o hücreye denk gelen yatay harf ile dikey harf birbirinin aynısı ise o hücreye bir nokta (dot / '1') konulur, değilse boş ('0') bırakılır.</p>
        <p>Matris tamamlandığında köşegende (diagonal) uzun ve kesintisiz çizgiler oluşuyorsa, diziler o bölgede büyük bir benzerliğe sahip demektir. Çapraz çizgide kaymalar (shift) varsa insersiyon/delesyon mutasyonlarını, ters yöne giden çapraz çizgiler varsa ters dönme (inversion) mutasyonlarını temsil eder. Dot plot, dinamik programlama hizalamalarına göre hesaplama açısından çok daha ucuz ama görsel açıdan çok daha zengin bir analiz aracıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>X ve Y dizilerinin harf kombinasyonlarından (Örn: X=3 harf, Y=3 harf) yola çıkarak 3x3 boyutlarında iki boyutlu (2D) bir ızgara oluşturmalıyız. Her bir koordinattaki (i,j) harfleri karşılaştırmalı, birbirlerine eşitse (Match) o koordinata 1 rakamını, farklıysa (Mismatch) 0 rakamını atamalıyız. Sonunda tamamen 0 ve 1'lerden oluşan dijital bir görüntü haritası elde etmeliyiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>İki boyutlu ızgara problemleri için standart yaklaşım \"İç İçe Geçmiş Döngüler\" (Nested For Loops) kurmaktır. Dıştaki döngü X dizisini tararken (satırları oluştururken), içteki döngü Y dizisini tarar (sütunları oluşturur). Optimizasyon kuralımız burada da geçerlidir: MATLAB'da bir matris adım adım (döngü içinde) büyütülmez. İşleme başlamadan önce <code>zeros()</code> fonksiyonu ile içi sıfır dolu kara bir tuval (blank canvas) oluşturulur ve sadece eşleşme bulunan yerler (beyaz pikseller/1) boyanır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Döngü kullanmadan <code>x == y'</code> gibi bir matris çarpımı (vektörel broadcast) matrisi tek satırda oluşturabilir, ancak Dot Plot analizi daha sonra gürültü filtreleme (pencereleme) gerektireceği için, döngülü yapı algoritmayı öğrenmek adına daha eğiticidir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>dot_matris = zeros(x_len, y_len);</code> : İşlem yapılacak bellek alanı hazırlanır. Tüm değerler zaten sıfır olduğu için, sonradan eşleşmeyen durumlar (Mismatch) için '0' atamaya (else bloğuna) gerek kalmaz.</li>
        <li><code>for i = 1:x_len</code> : Birinci dizinin her bir harfini temsil edecek satır indeksini (i) başlatan dış döngü.</li>
        <li><code>for j = 1:y_len</code> : İkinci dizinin her bir harfini temsil edecek sütun indeksini (j) başlatan iç döngü. (Yani i=1 iken j=1, 2, 3... diye döner).</li>
        <li><code>if x(i) == y(j)</code> : İlgili koordinattaki (Örn: satır 1 (A), sütun 2 (T)) harflerin karakter olarak eşit olup olmadığı sorgulanır.</li>
        <li><code>dot_matris(i, j) = 1;</code> : Eşitlerse, o koordinattaki (i,j) sıfır silinir ve nokta/piksel (1) konulur.</li>
        <li>Döngüler bitip matris ekrana yazdırılır (Gerçek uygulamalarda bu matris <code>imagesc()</code> fonksiyonu ile ekranda resim olarak çizdirilir).</li>
    </ul>
</div>
        """
    },
    {
        "id": "i19", "level": "intermediate",
        "title": "19. Nükleotid Ağırlığı (Moleküler Kütle) Hesaplama",
        "description": "<p>Bir DNA dizisinin yaklaşık moleküler ağırlığını (Da - Dalton veya g/mol) cinsinden hesaplayın. Tek sarmallı bir DNA için standart ağırlıklar şöyledir: A=313.2, C=289.2, G=329.2, T=304.2 (Geri kalan iskelet ağırlıkları dâhildir).</p><br/><p><b>Girdi:</b> <code>dna='ATGC'</code></p><p><b>Beklenen Çıktı:</b> <code>1235.8 Da</code></p>",
        "starter_code": "dna = 'ATGC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGC';\ntoplam_agirlik = 0;\n\nfor i = 1:length(dna)\n    nukleotid = dna(i);\n    switch nukleotid\n        case 'A'\n            toplam_agirlik = toplam_agirlik + 313.2;\n        case 'C'\n            toplam_agirlik = toplam_agirlik + 289.2;\n        case 'G'\n            toplam_agirlik = toplam_agirlik + 329.2;\n        case 'T'\n            toplam_agirlik = toplam_agirlik + 304.2;\n    end\nend\n\nfprintf('Moleküler Kütle: %.1f Da\\n', toplam_agirlik);",
        "expected_output": "Moleküler Kütle: 1235.8 Da",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Moleküler Ağırlık ve Oligo Sentezi)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Gerçek laboratuvar ortamında genetik materyaller (örneğin PCR için üretilen sentetik primerler veya kısa problar) kuru toz halinde sipariş edilir. Bu materyali uygun konsantrasyonda sıvı çözelti haline (örneğin 100 µM) getirebilmek için içine ne kadar su (Tampon - Buffer) katmanız gerektiğini bilmelisiniz. Bu hesaplamayı yapabilmek için de tüpün içinde bulunan DNA'nın kesin moleküler kütlesine (Ağırlığına) ihtiyacınız vardır.</p>
        <p>DNA molekülü sadece bazlardan (Adenin, Sitozin...) oluşmaz. Yan tarafında onu bir arada tutan bir şeker-fosfat iskeleti (Deoksiriboz ve Fosfat grubu) bulunur. A=313.2 Dalton değeri, sadece Adenin bazının değil, Adenin + Şeker + Fosfat (Deoksiadenozin monofosfat - dAMP) yapısının ağırlığıdır. Toplam kütleyi bulmak, biyoinformatik algoritmalarından daha çok deneysel moleküler biyolojinin (wet-lab) en temel destekleyici analizlerinden biridir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Programımız tek boyutlu bir karakter dizisini (DNA) alacak ve bir başlangıç ağırlığını (0) giderek artıracaktır (Accumulation). Dizinin başından sonuna doğru ilerlerken, karşılaştığı her harfe özel atanmış ondalıklı (float) kütle değerini ana toplama ekleyecektir. Sonunda dizinin toplam moleküler kütlesi ekrana basılacaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemi, her bir harfi baştan sayıp (Örn: A sayısı, C sayısı) bu sayıları ağırlıklarla çarparak ve sonuçları toplayarak da çözebilirsiniz (Vektörel Çarpım). Ancak bir karakterin sadece sınırlı sayıda spesifik (A, C, G, T) durum alabileceği senaryolarda <code>if-elseif-elseif-else</code> yapısı yerine <code>switch-case</code> yapısını kullanmak programlamada çok daha zarif ve hızlıdır. <code>switch-case</code> mekanizması karmaşık mantıksal sorgulamalar yapmaz, sadece verilen değere eşit olan kutuya (case) anında dallanır (branching).</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da (ve diğer dillerde) <code>switch</code> yapıları her zaman <code>otherwise</code> (diğer durumlar / default) isimli bir bloğa sahip olmalıdır. Eğer dizinin içine yanlışlıkla N veya X harfi karıştıysa, kodun çökmemesi veya yanlış hesap yapmaması için <code>otherwise</code> bloğunda hata mesajı verilebilir veya ağırlık atlaması yapılabilir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>toplam_agirlik = 0;</code> : Birikimli (accumulator) toplam kütle değişkenimiz sıfırdan başlar.</li>
        <li><code>for i = 1:length(dna)</code> : Dizideki her bir nükleotidi tek tek ziyaret edeceğimiz döngüyü kurarız.</li>
        <li><code>switch nukleotid</code> : Değişkenimizi yönlendirme mekanizmasına sokarız.</li>
        <li><code>case 'A'</code> : Eğer nükleotid değişkeni tam olarak 'A' karakterine eşitse buradaki kodlar çalışır ve toplam ağırlığa 313.2 eklenir. Diğer Case'ler es geçilir (C, C++, Java'daki gibi manuel <code>break</code> koymaya MATLAB'da gerek yoktur, her case kendi başına izoledir).</li>
        <li>Diğer üç harf için de ilgili kütle değerleri aynı mantıkla eklendikten sonra döngü başa döner.</li>
        <li><code>fprintf('... %.1f Da', toplam_agirlik);</code> : Sonuç virgülden sonra tek hane kalacak şekilde ondalıklı olarak ekrana basılır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i20", "level": "intermediate",
        "title": "20. Açık Okuma Çerçevesi (ORF) Çıkarma",
        "description": "<p>Bir DNA dizisinde protein sentezini başlatan ilk Başlangıç (Start) kodonunu (ATG) ve ondan sonra gelen ilk Bitiş (Stop) kodonunu (TAA, TAG, TGA) tespit edin. ATG'den başlayıp Stop kodonunda (Stop kodonu dâhil) biten geni (ORF - Open Reading Frame) dışarı çıkarın.</p><br/><p><b>Girdi:</b> <code>dna='CCATGGCATACTGACC'</code></p><p><b>Beklenen Çıktı:</b> <code>ATGGCATACTGA</code> (ATG'den başlar, TGA'da biter)</p>",
        "starter_code": "dna = 'CCATGGCATACTGACC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'CCATGGCATACTGACC';\norf_baslangic = -1;\norf_bitis = -1;\n\n% 1. Adım: İlk ATG'yi bul (Başlangıç)\nfor i = 1:length(dna)-2\n    if strcmp(dna(i:i+2), 'ATG')\n        orf_baslangic = i;\n        break; % İlkini bulunca çık\n    end\nend\n\n% 2. Adım: Başlangıçtan sonrasını 3'er 3'er okuyarak Stop kodonunu bul\nif orf_baslangic ~= -1\n    for i = orf_baslangic:3:length(dna)-2\n        kodon = dna(i:i+2);\n        if strcmp(kodon, 'TAA') || strcmp(kodon, 'TAG') || strcmp(kodon, 'TGA')\n            orf_bitis = i + 2; % Kodonun bittiği indeks (3. harf)\n            break; % İlk stop'ta bitir\n        end\n    end\nend\n\n% 3. Adım: Sonucu çıkar\nif orf_baslangic ~= -1 && orf_bitis ~= -1\n    orf = dna(orf_baslangic:orf_bitis);\n    disp(orf);\nelse\n    disp('Geçerli bir ORF bulunamadı.');\nend",
        "expected_output": "ATGGCATACTGA",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (ORF - Open Reading Frame)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bakteri genomları gibi büyük dizileri incelediğimizde, milyarlarca harfin tamamı protein kodlamaz. Hangi parçanın gerçek bir gen, hangi parçanın anlamsız (non-coding) bölge olduğunu bulmak genomik açıklamaların (Genome Annotation) temel amacıdır. Proteini oluşturan şifre dizisi, mRNA üzerinde her zaman bir <strong>Başlangıç Kodonu (ATG)</strong> ile başlar ve üç farklı <strong>Dur Kodonundan (TAA, TAG, TGA)</strong> biriyle sona erer. </p>
        <p>Başlangıç ve Bitiş kodonları arasında kalan, içinde başka hiçbir dur kodonu içermeyen ve ribozom tarafından kesintisiz okunabilen (üçün katları şeklinde olan) bu DNA parçasına <strong>Açık Okuma Çerçevesi (ORF - Open Reading Frame)</strong> denir. Gerçek gen bulma algoritmaları (Örn: GLIMMER, GeneMark), sadece bu ATG-Stop arasını bulmakla kalmaz, aynı zamanda bu boşluğun ne kadar uzun olduğuna bakar; eğer çok kısaysa tesadüf diyerek eler, uzun ve belirli GC oranlarına sahipse buraya \"Gen olma adayı\" damgası vurur.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize anlamsız karakterler içeren uzun bir metin verilmiştir. Algoritmamız iki aşamadan oluşmalıdır. Birinci aşamada, diziyi başından itibaren normal bir şekilde (1'er 1'er) tarayarak ilk gördüğü 'ATG' diziliminin indeksini kaydetmelidir (Çünkü ribozom başlangıcı nerede bulacağını bilemez). İkinci aşamada, artık başlangıç noktası bilindiği için, dizi bu noktadan (ATG) itibaren <strong>3'er 3'er (Kodon adımlarıyla)</strong> taranmalı ve karşısına ilk TAA, TAG veya TGA çıkana kadar gitmelidir. Bu iki noktanın arası kesilip ekrana basılacaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemde State Machine (Durum Makinesi) benzeri bir yaklaşım sergileriz. <code>orf_baslangic</code> isimli bayrak (flag) değişkenini -1 gibi imkansız bir indekse eşitleriz. ATG bulunduğunda bayrak güncellenir. Eğer bayrak -1 olarak kaldıysa, dizide hiç ATG yoktur ve Stop kodonu aramak manasızdır (Sistem hataya düşmesini engelleyen koruma mekanizması). Stop kodonu bulduğumuzda kaydettiğimiz indeks <code>i</code> değeri, kodonun ilk harfidir (örn: TGA'nın T'si). ORF dizisini tam almak için son harfi (A'yı) da içeri dahil etmek gerekir, bu yüzden <code>bitis = i + 2</code> matematiği uygulanır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da modern <code>regexp()</code> (Regular Expressions - Düzenli İfadeler) fonksiyonu ile bu problem tek satırda (<code>'ATG([ACTG]{3})*?(TAA|TAG|TGA)'</code>) çözülebilir. Ancak RegEx motorlarının çalışma mantığı oldukça karışıktır ve algoritmanın biyolojik arka planını (frame-shift mantığını) anlamak için For döngüsü ile (3'er adımlı) kodlamak çok daha eğiticidir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>orf_baslangic = -1;</code> : Başlangıç indeksinin bulunamadığını temsil eden başlangıç durumu.</li>
        <li><code>for i = 1:length(dna)-2</code> : İlk ATG'yi bulmak için 1'er 1'er ilerleyen birinci döngü. İlk ATG bulunduğunda indeks kaydedilir ve <code>break</code> ile döngüden hemen çıkılır.</li>
        <li><code>if orf_baslangic ~= -1</code> : Koruma kontrolü. ATG gerçekten bulunduysa aşağıdaki bloğa girilir.</li>
        <li><code>for i = orf_baslangic:3:length(dna)-2</code> : <strong>En kritik satır.</strong> Döngü 1'den değil, ATG'nin başladığı yerden (orf_baslangic) başlar ve artık 1'er değil 3'er atlar (Okuma çerçevesi oluşturulur).</li>
        <li><code>if strcmp(kodon, 'TAA') || ...</code> : Kesilen parçanın stop kodonlarından biri olup olmadığı kontrol edilir. </li>
        <li>Eğer stop ise, <code>orf_bitis = i + 2</code> ile son harfin indeksi işaretlenir ve bu döngü de kırılır.</li>
        <li>Eğer her iki işaret noktası da sağlıklı şekilde (-1'den farklı) bulunmuşsa, dizi <code>dna(baslangic:bitis)</code> mantığıyla kesilip ana ORF sekansı olarak ekrana basılır.</li>
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
