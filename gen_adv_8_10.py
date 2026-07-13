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
        "id": "a8", "level": "advanced",
        "title": "8. BLAST Seeding (Tohumlama) Algoritması: Tam Eşleşmeleri Bulma",
        "description": "<p>BLAST arama motorunun ilk adımı olan Seeding (Tohum) algoritmasının bir prototipini yazın. Büyük bir referans genom dizisi ve kısa bir sorgu (query) dizisi veriliyor. Sorgudaki k=3 uzunluğundaki her bir parçayı (word) referans genomda arayın. Eğer tam eşleşme (Exact Match) varsa, (Sorgu_İndeksi, Genom_İndeksi) çiftini ekrana yazdırarak bir Seed (Tohum) oluşturun.</p><br/><p><b>Girdi:</b> <code>genom='ATGCATGC', sorgu='TGC', k=3</code></p><p><b>Beklenen Çıktı:</b> Seed Bulundu! (Sorgu: 1, Genom: 2) | Seed Bulundu! (Sorgu: 1, Genom: 6)</p>",
        "starter_code": "genom = 'ATGCATGC';\nsorgu = 'TGC';\nk = 3;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "genom = 'ATGCATGC';\nsorgu = 'TGC';\nk = 3;\n\ngenom_len = length(genom);\nsorgu_len = length(sorgu);\n\n% 1. Adım: Sorguyu K-mer'lere ayır (Bu örnekte zaten 3 harf olduğu için tek parça çıkacak)\nfor i = 1:sorgu_len-k+1\n    sorgu_word = sorgu(i:i+k-1);\n    \n    % 2. Adım: Bu K-mer'i referans genom üzerinde kayarak ara\n    for j = 1:genom_len-k+1\n        genom_word = genom(j:j+k-1);\n        \n        % Tam eşleşme (Exact Match) kontrolü\n        if strcmp(sorgu_word, genom_word)\n            fprintf('Seed Bulundu! (Sorgu İndeksi: %d, Genom İndeksi: %d)\\n', i, j);\n        end\n    end\nend",
        "expected_output": "Seed Bulundu! (Sorgu İndeksi: 1, Genom İndeksi: 2)\nSeed Bulundu! (Sorgu İndeksi: 1, Genom İndeksi: 6)",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (BLAST Heuristic Yaklaşımı)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatik tarihinin tartışmasız en önemli algoritması 1990 yılında yayınlanan BLAST'tır (Basic Local Alignment Search Tool). Eğer elinizdeki 10.000 harflik bir geni, 3.2 milyar harflik İnsan Genomu ile hizalamak isterseniz, Smith-Waterman algoritması aylar sürer. BLAST bu sorunu çözmek için \"Heuristic\" (Sezgisel / Yaklaşık) bir yol izler. Felsefesi şudur: \"Eğer iki uzun dizi evrimsel olarak birbirine benziyorsa, bu dizilerin içinde en azından kısa bir bölge <strong>Birebir ve Kusursuz (Exact Match)</strong> olarak aynı olmak zorundadır.\" Bu kısa ve kusursuz eşleşmelere <strong>Seed (Tohum)</strong> denir.</p>
        <p>BLAST algoritması 3 aşamadan oluşur: 1) <strong>Seeding:</strong> Sorgu dizisini k-mer'lere (DNA için k=11, Protein için k=3) böler ve veritabanında bu kelimeleri birebir arayarak tohumları eker. 2) <strong>Extension (Genişletme):</strong> Sadece tohumların atıldığı yerleri hedefler (Milyarlarca harfi çöpe atar). Tohumun sağından ve solundan dışarıya doğru Smith-Waterman mantığıyla yavaş yavaş genişler. Eğer benzerlik devam ediyorsa puan artar. 3) <strong>Evaluation (Değerlendirme):</strong> Genişleme sırasında puan belirli bir eşiği aşarsa (Yüksek skorlu segment - HSP), bunu kullanıcıya istatistiksel bir p-değeri (E-value) ile sunar. İşte biz bu problemde, her şeyin başladığı o ilk kığılcımı, yani Seeding aşamasını kodluyoruz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Elimizde bir referans genom (Genellikle devasa olur) ve bir sorgu dizisi (Kısa) var. Öncelikle sorgu dizisini baştan sona k=3 boyutunda küçük kelimelere (Word) ayıracağız (Örneğin sorgumuz 5 harfliyse elimizde 3 adet word olacak). Daha sonra, bu küçük kelimelerden her birini alıp referans genomun üzerinde kayan pencere (sliding window) ile baştan sona arayacağız. Birebir tutan bir kelime gördüğümüz an, sorgudaki hangi kelimenin (indeks i), genomdaki hangi bölgeye (indeks j) yapıştığını (Seed) koordinat olarak kaydedeceğiz.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu temel kod, algoritmanın felsefesini anlamak için iç içe geçmiş iki döngü (O(N*M) karmaşıklığı) kullanır. Dış döngü sorguyu keser, iç döngü genomu tarar. Ancak gerçek BLAST yazılımı (NCBI C++ kod tabanı) asla böyle çalışmaz. İç içe döngüler yerine, genomdaki tüm k-mer'ler önceden devasa bir Hash Tablosuna (Sözlüğe) yüklenir. Sorgu kelimesi alındığında (Örn: TGC), döngüye girmeden direkt sözlüğe sorulur (<code>harita('TGC')</code>). Sözlük, O(1) hızında TGC'nin genomda hangi indekslerde olduğunu liste halinde verir. Hash tablosu oluşturmayı 16. Orta Seviye probleminde öğrenmiştik; bu problemde temel eşleşme mantığını oturtuyoruz.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> String dizilerini döngülerle kıyaslarken <code>strcmp()</code> kullanmak en güvenli yoldur ancak MATLAB'da <code>strfind()</code> (veya modern <code>strpos</code>) kullanırsanız, içteki <code>for</code> döngüsünü tamamen çöpe atabilir ve tek bir fonksiyon çağrısıyla o kelimenin genomdaki tüm lokasyonlarını saniyenin binde biri sürede vektörel olarak çekebilirsiniz.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>for i = 1:sorgu_len-k+1</code> : İlk döngümüz sorgu (query) dizisini parçalamak için çalışır. Eğer sorgu 'TGC' (3 harf) ve k=3 ise, bu döngü sadece 1 kere dönecektir.</li>
        <li><code>sorgu_word = sorgu(i:i+k-1);</code> : O turdaki arama terimini (Word) çıkarıyoruz.</li>
        <li><code>for j = 1:genom_len-k+1</code> : İkinci döngümüz referans genom üzerinde baştan sona doğru kayarak ilerler.</li>
        <li><code>genom_word = genom(j:j+k-1);</code> : Genomun o anki penceresindeki 3 harfi çekiyoruz.</li>
        <li><code>if strcmp(sorgu_word, genom_word)</code> : Tam eşleşme (Exact Match) var mı diye iki stringi kontrol ediyoruz. Match/Mismatch skorlaması burada YOKTUR, birebir aynı olmak zorundadır.</li>
        <li>Eğer eşitlik sağlanırsa, <code>fprintf</code> ile sorgunun i. indeksinden gelen kelimenin, genomun j. indeksine tam oturduğunu (Tohum atıldığını) sisteme raporluyoruz. </li>
    </ul>
</div>
        """
    },
    {
        "id": "a9", "level": "advanced",
        "title": "9. Markov Zinciri Modeli Eğitimi: Geçiş (Transition) Matrisi Çıkarma",
        "description": "<p>Bir DNA dizisi (Gözlem verisi) kullanılarak, Markov modelleri için gerekli olan Birinci Dereceden Geçiş Olasılıkları Matrisini (Transition Probability Matrix) hesaplayan bir kod yazın. (Örneğin A harfinden sonra C gelme ihtimali nedir?). Satırların toplamı 1 (veya %100) olmalıdır.</p><br/><p><b>Girdi:</b> <code>dna='ATGCAT'</code></p><p><b>Beklenen Çıktı:</b> 4x4 boyutunda A, C, G, T arası geçiş ihtimallerini ondalıklı (Örn: 0.50, 1.00) gösteren matris.</p>",
        "starter_code": "dna = 'ATGCAT';\nbazlar = ['A', 'C', 'G', 'T'];\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGCAT';\nbazlar = ['A', 'C', 'G', 'T'];\n\n% 4x4 boyutunda boş geçiş sayacı matrisi\ngecisler = zeros(4, 4);\n\n% Dizideki geçişleri sayma\nfor i = 1:length(dna)-1\n    simdiki_harf = dna(i);\n    sonraki_harf = dna(i+1);\n    \n    % Harflerin A,C,G,T içindeki indekslerini bulma (1, 2, 3 veya 4)\n    satir_indeks = find(bazlar == simdiki_harf);\n    sutun_indeks = find(bazlar == sonraki_harf);\n    \n    % Matristeki ilgili hücreyi 1 artır\n    gecisler(satir_indeks, sutun_indeks) = gecisler(satir_indeks, sutun_indeks) + 1;\nend\n\n% Sayıları Olasılığa (0 ile 1 arasına) çevirme (Normalizasyon)\nolasilik_matrisi = zeros(4, 4);\nfor i = 1:4\n    satir_toplami = sum(gecisler(i, :));\n    if satir_toplami > 0\n        olasilik_matrisi(i, :) = gecisler(i, :) / satir_toplami;\n    end\nend\n\ndisp('Geçiş Olasılıkları Matrisi (Satırlar: Mevcut Harf, Sütunlar: Sonraki Harf)');\ndisp(olasilik_matrisi);",
        "expected_output": "Geçiş Olasılıkları Matrisi\n         0         0         0    1.0000\n         0         0    1.0000         0\n         0    1.0000         0         0\n         0         0         0         0\n(ATGCAT için: A->T (1 kez), T->G (1 kez), G->C (1 kez), C->A (1 kez))",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Markov Zincirleri ve Model Eğitimi)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte Markov Zincirleri, gelecekteki bir durumun (DNA'daki bir sonraki nükleotidin) ne olacağının, <strong>sadece ve sadece içinde bulunulan anki duruma (şimdiki nükleotide)</strong> bağlı olduğunu varsayan stokastik (rastgelelik içeren) bir matematiksel modeldir. Yani A'dan sonra T gelme ihtimali bellidir, ancak o A'dan önce ne geldiğinin (geçmişin) hiçbir önemi yoktur. Buna Markov'un Belleksizlik Özelliği (Memorylessness) denir.</p>
        <p>Viterbi ve Forward algoritmalarında, geçiş olasılıklarını (Örn: A'dan G'ye %40) hep dışarıdan hazır bir sistem parametresi olarak aldık. Peki bilim insanları bu olasılıkları (Probability Parameters) en başta nereden buluyorlar? İşte bu rakamlar laboratuvarlarda uydurulmaz; devasa DNA veritabanları (Örneğin insan genomunun tamamı) bir bilgisayar programına verilir ve program bu genomu baştan sona okuyarak harflerin birbirini takip etme istatistiğini çıkarır. Bu işleme <strong>\"Model Eğitimi\" (Model Training / Parameter Estimation)</strong> denir. CpG adacıklarının tespit edilmesinin ardındaki mantık da budur; çünkü insan genomunda normalde C'den sonra G gelme ihtimali çok düşüktür, ancak metilasyon bölgelerinde (Adacıklarda) C'den sonra G gelme ihtimali anormal derecede yüksektir. Modeli eğitmek demek, bu frekans tablosunu çıkarmak demektir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız çok açıktır. Verilen dizi üzerinde baştan sona ilerleyeceğiz. Her adımda yan yana duran iki harfe bakacağız (Örn: A ve T). Bu, \"A'dan T'ye bir geçiş oldu\" demektir. 4x4 (A,C,G,T) boyutlarında sıfırlarla dolu bir Çetele Matrisi (Count Matrix) oluşturup, A satırı ile T sütununun kesiştiği kutuya bir çentik (1) atacağız. Tüm dizi bittiğinde elimizde mutlak frekansları gösteren bir çetele tablosu olacak. Ancak Markov matrisleri frekansları değil Olasılıkları (0 ile 1 arası değerleri) kullanır. Bu nedenle ikinci bir işlem olarak bu çeteleyi <strong>Normalize etmeliyiz</strong>. Matrisin her bir satırını toplayacak ve satırdaki her sayıyı o toplama bölerek yüzdeye/olasılığa çevireceğiz (Satır toplamı daima 1 olacak).</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>A'nın satır indeksinin 1, C'nin 2, G'nin 3 ve T'nin 4 olduğunu bulmak için <code>find()</code> fonksiyonunu harf dizisi (<code>['A', 'C', 'G', 'T']</code>) üzerinde mantıksal sorgu ile kullanırız. Ancak eğer diziniz milyarlarca harf uzunluğundaysa, her harfte <code>find()</code> çağırmak çok pahalıdır. İleri seviye bir C++ veya MATLAB mühendisi bunu çözmek için bir Hash Map kullanır ya da harflerin ASCII kod değerlerini manipüle ederek (Örn: harf - 65) indeksleri bir matematiksel formul ile O(1) hızında bulur. Normalizasyon aşamasında (bölme işleminde), eğer bir satırda hiç sayı yoksa (örn dizide hiç T harfi yoksa T'den başka yere geçiş de olmaz) satır toplamı 0 olur. MATLAB'da 0'a bölmek kodu çökertmese de <code>NaN</code> döner ve matrisi bozar. Bu nedenle <code>if satir_toplami > 0</code> koruması yazmak şarttır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da bir matrisin belirli bir satırındaki tüm elemanlara aynı anda ulaşmak için kolon operatörü (<code>:</code>) kullanılır. <code>gecisler(i, :)</code> ifadesi, i. satırın tamamı (Tüm sütunları) anlamına gelir. Normalizasyon döngüsündeki bölme işlemi, iç içe for döngülerinden kurtarılarak tamamen vektörize edilmiştir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>gecisler = zeros(4, 4);</code> : 4 harfin birbirine geçişlerini (Örn: A->A, A->C, A->G, A->T) tutacak 16 hücreli çetele matrisimizi sıfırlıyoruz.</li>
        <li><code>for i = 1:length(dna)-1</code> : Diziyi tarıyoruz. Sınırın (N-1) olma sebebi, son harfin ardından geçilecek başka bir harf kalmamasıdır (Eğer döngüyü sona dayarsanız Index Out of Bounds hatası alırsınız).</li>
        <li><code>simdiki_harf = dna(i); sonraki_harf = dna(i+1);</code> : Geçiş yapan çiftleri alıyoruz.</li>
        <li><code>satir_indeks = find(bazlar == simdiki_harf);</code> : Bulunduğumuz harfin vektörde kaçıncı sırada (1, 2, 3, 4) olduğunu bulup bunu Satır numarası olarak belirliyoruz.</li>
        <li><code>gecisler(satir_indeks, sutun_indeks) = gecisler(...) + 1;</code> : Satır ve Sütunun kesiştiği o hücredeki sayıyı bir artırıyoruz. Artık elimizde frekans matrisi var.</li>
        <li><strong>Normalizasyon Bloğu:</strong> Olasılık (Probability) matrisini oluşturuyoruz. 4 satır için döngü başlatıyoruz.</li>
        <li><code>satir_toplami = sum(gecisler(i, :));</code> : A harfinden toplamda kaç kez çıkış yapıldığını buluyoruz. Örneğin A'dan C'ye 3, T'ye 1 geçiş varsa toplam çıkış 4'tür. O zaman A->C geçiş olasılığı 3/4 = %75'tir.</li>
        <li><code>olasilik_matrisi(i, :) = gecisler(i, :) / satir_toplami;</code> : Satırdaki tüm elemanları yatay bir vektör halinde tek seferde alıp satır toplamına bölüyoruz ve olasılık matrisine yazıyoruz. Markov Transition Matrisimiz hazırdır.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a10", "level": "advanced",
        "title": "10. Burrows-Wheeler Dönüşümü (BWT): Döngüsel Kaydırma (Circular Shift)",
        "description": "<p>Modern yeni nesil dizileme (NGS) hizalamalarında (Örn: BWA ve Bowtie yazılımlarında) indeksleme için Burrows-Wheeler Dönüşümü (BWT) kullanılır. BWT'nin en zorlu ilk aşaması, verilen DNA dizisinin harf harf tüm \"Döngüsel Kaydırmalarını (Circular Shifts)\" oluşturmak ve ardından bu kaydırılmış dizileri alfabetik (sözlük) sırasına göre sıralayarak BWT Matrisini oluşturmaktır. Bu hazırlık kodunu yazın.</p><br/><p><b>Girdi:</b> <code>dna='ATGC$'</code> (BWT'de sonu belli etmek için genelde $ sembolü eklenir)</p><p><b>Beklenen Çıktı:</b><br/>$ATGC<br/>C$ATG<br/>GC$AT<br/>... vb.</p>",
        "starter_code": "dna = 'ATGC$';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGC$';\nuzunluk = length(dna);\n\n% Kaydırılmış kelimeleri tutmak için Hücre Dizisi (Cell Array)\nkaydirmalar = cell(uzunluk, 1);\n\n% 1. Adım: Tüm döngüsel kaydırmaları oluştur\nfor i = 1:uzunluk\n    % Başlangıçtan i'ye kadar olanı sona at, kalanını başa al\n    bas = dna(1:i-1);\n    son = dna(i:end);\n    \n    kaydirilmis_dizi = [son, bas];\n    kaydirmalar{i} = kaydirilmis_dizi;\nend\n\n% 2. Adım: Kaydırılmış dizileri alfabetik (sözlük) sırasına diz (Lexicographical Sorting)\nsirali_bwt_matrisi = sort(kaydirmalar);\n\ndisp('Burrows-Wheeler Alfabetik Kaydırma Matrisi:');\nfor i = 1:uzunluk\n    disp(sirali_bwt_matrisi{i});\nend\n\n% Not: Gerçek BWT dizisi, bu sıralı matrisin en son (en sağ) sütunundaki harflerdir.",
        "expected_output": "Burrows-Wheeler Alfabetik Kaydırma Matrisi:\n$ATGC\nATGC$\nC$ATG\nGC$AT\nTGC$A",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Burrows-Wheeler Transform ve BWA Algoritması)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>BLAST algoritması harika çalışsa da, 2005 yılından sonra ortaya çıkan Yeni Nesil Sekanslama (NGS - Illumina) cihazlarının ürettiği devasa veriler (tek bir seferde yüz milyonlarca kısa DNA parçası - read) için BLAST bile fazla yavaş kalıyordu. Yüz milyonlarca 100 harflik parçayı, 3 milyar harflik insan genomuna hizalamak için bambaşka bir matematiksel mimari gerekti. İşte 1994 yılında Michael Burrows ve David Wheeler tarafından veri sıkıştırma (bzip2) amacıyla icat edilen BWT algoritması, Heng Li tarafından <strong>BWA (Burrows-Wheeler Aligner)</strong> adıyla genom hizalamaya uyarlandı ve biyoinformatik tarihinde yeni bir devrim yarattı.</p>
        <p>BWT'nin sırrı şudur: Çok uzun bir DNA dizisinin BWT Dönüşümünü aldığınızda, dizinin içindeki aynı harfler bir araya toplanır (örneğin arka arkaya yüzlerce A). Bu, diziyi inanılmaz derecede sıkıştırılabilir (Sonek Ağaçları / Suffix Arrays) hale getirir ve arama işlemlerinin (hizalamanın) O(Genom Uzunluğu) hızında değil, sadece O(Sorgu Uzunluğu) hızında yapılmasını sağlar! Bu, insan genomunda arama yapmanın, bir kelimeyi küçük bir şiirde aramakla aynı sürede (saliseler içinde) bitmesi demektir. BWT dönüşümü yapmak için önce metnin sonuna her harften (alfabetik olarak) daha küçük sayılan bir sonlandırma sembolü (Genellikle $) eklenir. Ardından metnin tüm varyasyonları kaydırılır, alfabetik sıraya sokulur ve oluşan bu sihirli matrisin sadece en sağ sütunundaki harfler alınarak BWT dizisi oluşturulur. Biz bu devrimin ilk yarısını, BWT sıralı matrisini oluşturmayı kodlayacağız.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Girdi olarak sonuna '$' eklenmiş bir metin alacağız. Birinci adımda bu kelimenin kendisi kadar (Örn 5 harfliyse 5 adet) varyasyonunu çıkaracağız. Bunu döngüsel kaydırma (Circular Shift) ile yapacağız: Baştaki harfi koparıp en sona ekleyeceğiz (Örn: ATGC$ -> TGC$A -> GC$AT). İkinci adımda, bu oluşturduğumuz 5 kelimeyi alt alta bir liste (hücre dizisi) haline getireceğiz ve bilgisayar bilimlerinin standart Alfabetik (Lexicographical) sıralama işleminden geçireceğiz. En küçük sembol '$' olduğu için en üste o geçecek, sonra A, sonra C gibi sıralanacaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Sürekli değişen ve boyutu dinamik karakter dizilerini tutmak için <code>cell()</code> (Hücre dizisi) yaratmak en iyi yoldur. Normal bir 2D char matrisi karakter boyutları değiştiğinde hata verebilir ancak cell yapısı her şeyi yutar. Karakterleri kaydırmak (Shift) için MATLAB'ın yerleşik <code>circshift()</code> fonksiyonu kullanılabilirdi. Ancak string dilimleme (String Slicing) mantığını (<code>bas</code> ve <code>son</code> olarak ikiye bölüp <code>[son, bas]</code> şeklinde yer değiştirme) göstermek eğitim açısından önemlidir. İşin en güzel yanı, MATLAB'ın <code>sort()</code> fonksiyonunun, içine bir hücre dizisi (Cell array of strings) atıldığında varsayılan (default) olarak Lexicographical (Sözlük sırası) algoritmalarıyla otomatik olarak sıralamasıdır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Gerçek BWA (Burrows-Wheeler Aligner) uygulamalarında 3 milyar harflik genomun (insan genomu) BWT'si alınırken bu şekilde bir Matris bellekte oluşturulmaz. 3 milyar x 3 milyar bir matris oluşturmak petabaytlarca RAM gerektirir (Ram taşması - Out of Memory). Bunun yerine Sonek Dizileri (Suffix Arrays) kullanılarak matris hiç oluşturulmadan, sadece matematiksel indeks numaraları alfabetik olarak sıralanır ve sonuç elde edilir. Biyoinformatiğin asıl gücü bu algoritma tasarımlarında yatar.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>kaydirmalar = cell(uzunluk, 1);</code> : 5 satırlı, 1 sütunlu boş bir hücre dizisi yaratılarak ön tahsis (pre-allocation) yapılır.</li>
        <li><code>for i = 1:uzunluk</code> : Dizinin harf sayısı kadar kaydırma (shift) yapılacaktır.</li>
        <li><code>bas = dna(1:i-1);</code> : Dizinin birinci harfinden o anki kaydırma sınırına kadar olan kısmını (Örn: sadece 'A' veya 'AT') kesip koparır.</li>
        <li><code>son = dna(i:end);</code> : Geriye kalan kuyruk kısmını (Örn: 'TGC$') keser.</li>
        <li><code>kaydirilmis_dizi = [son, bas];</code> : Kuyruk kısmı (son) öne alınır, baştan kestiğimiz parça arkaya takılır. Böylece eksiksiz bir döngüsel kaydırma uygulanmış olur.</li>
        <li><code>kaydirmalar{i} = kaydirilmis_dizi;</code> : Elde edilen yeni varyasyon haritaya kaydedilir.</li>
        <li><code>sirali_bwt_matrisi = sort(kaydirmalar);</code> : Haritadaki kelimeler MATLAB'ın ASCII sıralama algoritmasına göre A'dan Z'ye sıralanır. '$' işareti ASCII tablosunda harflerden önce geldiği için en üst satırı alır.</li>
        <li>İşlem ekrana basılarak BWT matrisinin son hali gösterilir. Literatürdeki BWT dizisi, bu listelenen kelimelerin sadece en son harflerinin alt alta alınmasıyla oluşturulan dizidir (Bu örnek için: CGT$A).</li>
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
