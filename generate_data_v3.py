# coding: utf-8
import json

base_exp = """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan</h4>
    <div style="margin-top: 1rem;">{bio}</div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem;">{problem_def}</div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem;">{matlab_logic}</div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> {tip}
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        {steps}
    </ul>
</div>
"""

p_data = [
  {
   "title": "DNA'dan RNA'ya Transkripsiyon", "inp": "ATGCGTACGTCG", "out": "AUGCGUACGUCG",
   "desc": "DNA dizisini RNA'ya çeviren (T -> U) MATLAB kodunu yazın.",
   "code": "dna = 'ATGCGTACGTCG';\nrna = strrep(dna, 'T', 'U');\ndisp(rna);",
   "bio": "<p>Hücrenin çekirdeğinde bulunan DNA, organizmanın tüm genetik şifresini taşır. Ancak protein sentezi (translasyon) sitoplazmadaki ribozomlarda gerçekleşir. DNA'nın çekirdekten çıkamaması nedeniyle, ilgili gen bölgesinin genetik şifresi haberci RNA (mRNA) molekülüne kopyalanır. Bu kopyalama işlemine <strong>Transkripsiyon (Yazılma)</strong> denir.</p><p>Kimyasal yapı olarak RNA, DNA'dan iki temel farklılık gösterir: Birincisi şeker yapısı (Deoksiriboz yerine Riboz), ikincisi ise baz yapısıdır. DNA'da bulunan Timin (T) bazı, RNA'da bulunmaz; bunun yerine <strong>Urasil (U)</strong> bazı gelir. Biyoinformatik analizlerde bu biyokimyasal farklılık, karakter dizilerinde basit bir harf değişimi olarak modellenir.</p>",
   "problem_def": "<p>Bize girdi olarak sadece A, C, G ve T karakterlerinden oluşan bir metin dizisi (string) verilmektedir. Amacımız, diziyi baştan sona taramak ve karşılaştığımız her 'T' karakterini 'U' karakteri ile değiştirmektir. Çıktı olarak yeni oluşan RNA dizisini döndürmemiz gerekmektedir.</p>",
   "matlab_logic": "<p>Bu problem, bilgisayar bilimlerinde klasik bir \"Bul ve Değiştir\" (Find and Replace) problemidir. MATLAB'da karakter dizileri (char arrays veya strings) üzerinde bu işlemi yapmak için döngüler (for/while) kullanmak mümkündür, ancak MATLAB'ın gücü vektörel operasyonlardan gelir. MATLAB'ın yerleşik <code>strrep</code> fonksiyonu, bu işlemi C seviyesinde son derece hızlı bir şekilde gerçekleştirir.</p>",
   "tip": "Büyük genomik verilerle çalışırken döngü kullanmaktan kaçının. Milyonlarca baz çifti içeren bir kromozom dizisinde for döngüsü ile T aramak dakikalar alabilirken, <code>strrep</code> fonksiyonu saniyenin küçük bir kesrinde bu işlemi tamamlar.",
   "steps": "<li><code>dna = 'ATGCGTACGTCG';</code> : DNA dizisini bellekte bir karakter dizisi (char array) olarak <code>dna</code> değişkenine atıyoruz.</li><li><code>rna = strrep(dna, 'T', 'U');</code> : <code>strrep</code> fonksiyonu üç parametre alır. Birinci parametre işlem yapılacak değişken, ikinci parametre aranacak hedef ('T'), üçüncü parametre ise yeni değerdir ('U'). Fonksiyon tüm T'leri U'ya çevirip yeni diziyi <code>rna</code> değişkenine atar.</li><li><code>disp(rna);</code> : Sonuç dizisini MATLAB komut penceresinde (veya arayüzümüzde) ekrana basıyoruz.</li>"
  },
  {
   "title": "GC İçeriği Hesaplama", "inp": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT", "out": "%59.09",
   "desc": "DNA dizisindeki Guanin ve Sitozin yüzdesini hesaplayın.",
   "code": "dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT';\ng = sum(dna == 'G');\nc = sum(dna == 'C');\nuzunluk = length(dna);\ngc = ((g + c) / uzunluk) * 100;\nfprintf('%%%.2f\\n', gc);",
   "bio": "<p>Çift sarmallı DNA yapısında Adenin (A) daima Timin (T) ile eşleşirken, Guanin (G) daima Sitozin (C) ile eşleşir. Termodinamik açıdan A-T eşleşmesi iki hidrojen bağı oluştururken, G-C eşleşmesi üç hidrojen bağı oluşturur. Bu biyokimyasal gerçek, G-C oranı yüksek olan DNA sarmallarının birbirinden ayrılmak için daha yüksek ısı enerjisine ihtiyaç duymasına neden olur.</p><p>Laboratuvar ortamında DNA'yı çoğaltmak için kullanılan PCR (Polimeraz Zincir Reaksiyonu) testlerinde, tasarlanan primerlerin GC içeriğinin %40 ile %60 arasında olması istenir. GC içeriğinin hesaplanması, dizinin kararlılığını ölçmenin en basit ve en yaygın yoludur.</p>",
   "problem_def": "<p>Verilen bir karakter dizisinde toplam 'G' ve 'C' karakterlerinin sayısını bulmamız, bu toplamı dizinin toplam uzunluğuna bölmemiz ve 100 ile çarparak bir yüzde değeri elde etmemiz gerekmektedir.</p>",
   "matlab_logic": "<p>MATLAB'da karakterleri saymak için mantıksal indeksleme (logical indexing) kullanılır. <code>dizi == 'Karakter'</code> ifadesi, dizinin her bir elemanını kontrol eder ve eşleşme olan yerlere 1 (true), olmayan yerlere 0 (false) yazar. Oluşan bu 1 ve 0'lardan oluşan mantıksal matrisi <code>sum()</code> fonksiyonu ile topladığımızda, o karakterin dizide kaç kez geçtiğini direkt bulmuş oluruz.</p>",
   "tip": "Aritmetik işlemlerde parantez kullanımına dikkat edin. <code>g + c / uzunluk</code> yazmak sadece c'yi bölerken, <code>(g + c) / uzunluk</code> toplamı böler. İşlem önceliği hataları mantıksal hatalara yol açar.",
   "steps": "<li><code>g = sum(dna == 'G');</code> : DNA dizisindeki G'lerin yerini mantıksal (1/0) olarak bulur ve <code>sum</code> ile toplayarak toplam G sayısını <code>g</code> değişkenine atar.</li><li><code>c = sum(dna == 'C');</code> : Aynı mantıkla C karakterlerinin sayısını bulur.</li><li><code>uzunluk = length(dna);</code> : Dizinin toplam nükleotid sayısını (karakter uzunluğunu) hesaplar.</li><li><code>gc = ((g + c) / uzunluk) * 100;</code> : G ve C sayılarını toplayıp toplam uzunluğa böler ve yüzde formatına çevirir.</li><li><code>fprintf('%%%.2f\\n', gc);</code> : Sonucu virgülden sonra iki hane kalacak şekilde (<code>.2f</code>) ve başına yüzde işareti koyarak (MATLAB'da % işareti basmak için <code>%%</code> kullanılır) ekrana yazdırır.</li>"
  },
  {
   "title": "Nükleotid Sayımı", "inp": "AGCTTTTCATTCTGACTGCA...", "out": "A: 20, C: 12, G: 17, T: 21",
   "desc": "Dizideki A, C, G, T nükleotidlerinin sayılarını ayrı ayrı bulun.",
   "code": "dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC';\na=sum(dna=='A'); c=sum(dna=='C'); g=sum(dna=='G'); t=sum(dna=='T');\nfprintf('A: %d, C: %d, G: %d, T: %d\\n', a, c, g, t);",
   "bio": "<p>Genomların baz kompozisyonu (hangi nükleotidden ne kadar olduğu), canlı türleri arasında büyük farklılıklar gösterir. Örneğin bazı bakterilerin genomları GC açısından çok zenginken, bazıları AT açısından zengindir. Belirli bir DNA dizisindeki dört nükleotidin mutlak sayısının bilinmesi, o dizinin istatistiksel profilini çıkarmak için ilk adımdır.</p><p>Ayrıca, baz kompozisyonundaki asimetriler (skew), replikasyon başlangıç noktalarının (origin of replication) tahmin edilmesinde kullanılır.</p>",
   "problem_def": "<p>DNA metin dizisini okumalı ve içindeki her bir alfabenin (A, C, G, T) ayrı ayrı frekansını (geçiş sayısını) saymalıyız. Sonunda bu dört sayıyı okunaklı bir formatta yazdırmalıyız.</p>",
   "matlab_logic": "<p>Bir önceki problemde kullandığımız mantıksal toplama (logical sum) işlemini bu kez dört farklı karakter için dört ayrı değişkende uygulayacağız. Çıktı formatı için <code>disp</code> yerine daha kontrollü olan <code>fprintf</code> fonksiyonunu kullanarak tüm sayıları tek bir satıra yerleştireceğiz.</p>",
   "tip": "Çok uzun dizilerde her karakter için ayrı bir geçiş yapmak (4 defa diziyi taramak) yavaş olabilir. Daha ileri seviyelerde, `histcounts` veya `tabulate` gibi tek geçişli istatistiksel fonksiyonlar kullanarak bu işlem daha da optimize edilebilir.",
   "steps": "<li>Diziyi belleğe alın.</li><li><code>a=sum(dna=='A');</code> : Diziyi tarayarak A nükleotidlerini sayın ve <code>a</code> değişkenine atayın.</li><li>Bu işlemi C, G ve T için de sırasıyla tekrarlayarak <code>c</code>, <code>g</code>, ve <code>t</code> değişkenlerini oluşturun.</li><li><code>fprintf</code> komutundaki <code>%d</code> yer tutucuları, tam sayılar (integer) içindir. Verilen sırayla a, c, g, t değişkenleri bu yer tutucuların içine yerleştirilerek ekrana basılır.</li>"
  },
  {
   "title": "DNA Uzunluğunu Bulma", "inp": "ATCGATCGATCG", "out": "12",
   "desc": "Verilen DNA dizisinin nükleotid bazındaki toplam uzunluğunu ekrana yazdırın.",
   "code": "dna = 'ATCGATCGATCG';\ndisp(length(dna));",
   "bio": "<p>Bir genin veya kromozomun uzunluğu, biyolojide genellikle Baz Çifti (Base Pair - bp) cinsiyle ifade edilir. Örneğin insan genomu yaklaşık 3.2 milyar baz çiftinden oluşurken, basit bir virüs genomu birkaç bin baz çiftinden oluşabilir. Uzunluk verisi, dizinin türünü sınıflandırmakta ve analiz sırasında bellek gereksinimlerini hesaplamakta kullanılır.</p>",
   "problem_def": "<p>Sadece dizideki toplam karakter sayısını saymamız gerekmektedir. Uzunluk tam sayı bir değer olarak geri dönmelidir.</p>",
   "matlab_logic": "<p>MATLAB bir metin dizisini (string) aslında tek boyutlu bir karakter dizisi (1xN boyutunda bir vektör) olarak görür. Vektörlerin en büyük boyutunun uzunluğunu bulmak için <code>length()</code> fonksiyonu standarttır.</p>",
   "tip": "Diziniz çok boyutlu bir matris veya string array ise (birden fazla DNA dizisi içeriyorsa), <code>length</code> yanıltıcı olabilir; böyle durumlarda <code>strlength</code> (string uzunlukları) veya <code>size</code> kullanmak daha güvenlidir.",
   "steps": "<li><code>length(dna)</code> : MATLAB yerleşik fonksiyonunu çağırarak 1xN vektörünün N değerini (karakter sayısını) elde ediyoruz.</li><li>Elde edilen değeri <code>disp()</code> ile doğrudan komut penceresine yazdırıyoruz.</li>"
  },
  {
   "title": "Ters Çevrilmiş DNA Dizisi", "inp": "ATGC", "out": "CGTA",
   "desc": "DNA dizisini sondan başa doğru (ters olarak) okuyan bir kod yazın.",
   "code": "dna = 'ATGC';\nters = reverse(dna);\ndisp(ters);",
   "bio": "<p>DNA sarmalının yönlülüğü vardır; moleküler olarak 5' ucundan 3' ucuna doğru uzanır. Gen dizilim (sekanslama) teknolojilerinde, cihaz bazen DNA'yı beklenen yönde değil, ters yönde okuyabilir. Bu ters okumaları düzeltebilmek veya diziyi tersten analiz etmek biyoinformatik ön işlemlerinin parçasıdır.</p>",
   "problem_def": "<p>Karakter dizisinin başından sonuna doğru giden sıralamayı tam tersine çevirerek (son harfi ilk harf yaparak) yeni bir dizi oluşturmalıyız.</p>",
   "matlab_logic": "<p>MATLAB 2016b ve sonrası sürümlerde karakter ve metin işlemleri için <code>reverse()</code> fonksiyonu eklenmiştir. Eski sürümlerde ise vektör indeksleme kullanılarak <code>dizi(end:-1:1)</code> şeklinde, yani 'sondan başla, -1 adım geri git, 1. elemana kadar ilerle' mantığı kullanılırdı.</p>",
   "tip": "Matris indeksleme <code>(end:-1:1)</code> yöntemi, sadece metinlerde değil her türlü sayısal vektörü ters çevirmekte de kullanabileceğiniz temel ve güçlü bir MATLAB yeteneğidir.",
   "steps": "<li><code>reverse(dna)</code> fonksiyonu ile dizinin ayna görüntüsü alınır.</li><li>Alternatif olarak <code>dna(end:-1:1)</code> yazılsaydı: MATLAB dizinin son elemanından (end) başlar, -1'er adım geri gelir ve ilk elemana kadar diziyi yeniden oluştururdu.</li><li>Sonuç ekrana basılır.</li>"
  },
  {
   "title": "Ters Tamamlayıcı (Reverse Complement)", "inp": "AAAACCCGGT", "out": "ACCGGGTTTT",
   "desc": "Bir DNA dizisinin ters tamamlayıcısını (A->T, C->G yapıp tersine çevirme) bulun.",
   "code": "dna = 'AAAACCCGGT';\nt = dna;\nt(dna=='A')='T';\nt(dna=='T')='A';\nt(dna=='C')='G';\nt(dna=='G')='C';\nters_tamamlayici = t(end:-1:1);\ndisp(ters_tamamlayici);",
   "bio": "<p>Çift iplikli DNA'da bir iplik 5' → 3' yönünde ilerlerken, karşı iplik (tamamlayıcı iplik) ona antiparalel olarak 3' → 5' yönünde ilerler. Gen veritabanlarında (GenBank vb.) genellikle sadece tek bir iplik (sense strand) saklanır. Diğer ipliğin dizilimini bulmak için mevcut dizinin önce tamamlayıcısı (A yerine T, C yerine G) alınır, sonra antiparalel yönlülükten dolayı dizi tersine çevrilir. Bu işleme <strong>Reverse Complement</strong> denir ve primer tasarımı ile gen hizalama algoritmalarında sürekli kullanılır.</p>",
   "problem_def": "<p>Önce her bir harfi biyolojik eşleniğine dönüştürmeli, sonrasında elde edilen diziyi sondan başa doğru ters çevirmeliyiz.</p>",
   "matlab_logic": "<p>Eğer <code>strrep</code> kullansaydık, A'ları T yaptıktan sonra, T'leri A yapmaya çalıştığımızda az önce değiştirdiğimiz A'ları da geri çevirme riskimiz olurdu. Bu yüzden orijinal diziyi bir maske (referans) olarak kullanıp, geçici kopya dizi üzerinde mantıksal atamalar yapmak en güvenilir ve hatasız algoritmadır.</p>",
   "tip": "MATLAB'ın Bioinformatics Toolbox eklentisinde bu işlemi tek komutla yapan <code>seqrcomplement()</code> fonksiyonu vardır, ancak algoritma mantığını anlamak için bunu kendimiz yazmalıyız.",
   "steps": "<li><code>t = dna;</code> : Üzerinde değişiklik yapacağımız geçici kopya diziyi oluşturuyoruz.</li><li><code>t(dna=='A') = 'T';</code> : Orijinal <code>dna</code> dizisinde 'A' olan indekslere bakıyoruz ve kopyamız olan <code>t</code> dizisindeki o indekslere 'T' yazıyoruz. Bu sayede sadece baştaki A'lar değişiyor.</li><li>Bu maskeleme ve değiştirme işlemini T, C ve G için tekrarlayarak tamamen tamamlayıcı ipliği oluşturuyoruz.</li><li><code>t(end:-1:1)</code> ile elde ettiğimiz tamamlayıcı ipliği yön olarak tersine (5'->3' yönüne) çeviriyoruz.</li><li>Sonucu yazdırıyoruz.</li>"
  },
  {
   "title": "RNA'dan DNA'ya Ters Transkripsiyon", "inp": "AUGGCUACUUAA", "out": "ATGGCTACTTAA",
   "desc": "RNA dizisini tekrar DNA'ya çeviren (U -> T) bir kod yazın.",
   "code": "rna = 'AUGGCUACUUAA';\ndna = strrep(rna, 'U', 'T');\ndisp(dna);",
   "bio": "<p>Normal şartlarda bilgi akışı DNA'dan RNA'ya doğrudur. Ancak Retrovirüsler (örneğin HIV virüsü), RNA tabanlı genomlara sahiptir. Konağın (insan vb.) hücresine girdiklerinde, <strong>Ters Transkriptaz (Reverse Transcriptase)</strong> adlı enzimlerini kullanarak kendi RNA'larından DNA sentezlerler. Bu sentezlenen DNA daha sonra konağın genomuna entegre olur. Biyoinformatikte RNA tabanlı verileri DNA dizileme veritabanlarıyla karşılaştırmak için yazılımsal olarak ters transkripsiyon yaparız.</p>",
   "problem_def": "<p>Verilen RNA metin dizisindeki tüm 'U' karakterlerini bularak onları 'T' karakteri ile değiştirmeliyiz.</p>",
   "matlab_logic": "<p>İlk problemin (Transkripsiyon) tam tersidir. Tek yapmamız gereken hedef ve yeni değer parametrelerinin yerini değiştirmektir. <code>strrep</code> yine en efektif çözüm aracımızdır.</p>",
   "tip": "Sadece bir karakter değişimi olduğu için basit görünse de, binlerce sekansın aynı anda işlendiği veri setlerinde vektörel araçların kullanımı işlem süresini saatlerden saniyelere indirir.",
   "steps": "<li>RNA dizisini tanımlıyoruz.</li><li><code>strrep</code> fonksiyonu ile 'U' parametresini aratıp yerine 'T' koyuyoruz.</li><li>Elde edilen cDNA (komplementer DNA) dizisini ekrana basıyoruz.</li>"
  },
  {
   "title": "Motif Arama", "inp": "GATATATGCATATACTT (aranan: ATGC)", "out": "8",
   "desc": "Büyük bir dizi içinde belirli bir motifin başladığı indeksi bulun.",
   "code": "dna = 'GATATATGCATATACTT';\nmotif = 'ATGC';\nindeks = strfind(dna, motif);\ndisp(indeks);",
   "bio": "<p>Genlerin ifade edilip edilmemesini kontrol eden düzenleyici proteinler (Transkripsiyon Faktörleri), DNA üzerinde rastgele yerlere değil, belirli kısa şifrelere bağlanırlar. Bu kısa anlamlı dizilere <strong>Motif</strong> denir. TATA Kutusu (TATA Box) buna klasik bir örnektir. Bir gen bölgesinde bu motiflerin nerede başladığını bulmak, gen regülasyonunu anlamanın anahtarıdır.</p>",
   "problem_def": "<p>Büyük bir ana karakter dizisinin içinde, verilen alt dizinin (substring) nerede bulunduğunu (başlangıç konumunu/indeksini) bulmamız gerekmektedir.</p>",
   "matlab_logic": "<p>Metin içinde alt metin aramak için MATLAB'ın standart komutu <code>strfind</code>'dir. Bu fonksiyon, eğer motif birden fazla yerde geçiyorsa, sadece bir sayı değil, motifin başladığı tüm indekslerin konumlarını bir vektör (array) olarak döndürür.</p>",
   "tip": "Eğer motif dizinin içinde hiç geçmiyorsa, <code>strfind</code> boş bir vektör <code>[]</code> döndürür. İleri düzey kodlamada bunu bir <code>isempty()</code> kontrolü ile yakalamak iyi bir programlama pratiğidir.",
   "steps": "<li>Diziyi ve aranacak motifi belleğe alıyoruz.</li><li><code>strfind(dna, motif)</code> komutunu çalıştırarak motifin dizide geçtiği tüm başlangıç koordinatlarını çıkarıyoruz. (Bu örnekte indeks 8'den itibaren ATGC başlıyor).</li><li>İndeks değerini yazdırıyoruz.</li>"
  },
  {
   "title": "Sadece Pürinleri Filtreleme", "inp": "ATCGATCG", "out": "A G A G",
   "desc": "Dizideki pürinleri (A, G) koruyup, pirimidinleri boşluk (' ') ile değiştirin.",
   "code": "dna = 'ATCGATCG';\npurinler = dna;\npurinler(dna == 'T' | dna == 'C') = ' ';\ndisp(purinler);",
   "bio": "<p>DNA'yı oluşturan azotlu organik bazlar kimyasal yapılarına göre iki aileye ayrılır. <strong>Pürinler</strong> (Adenin ve Guanin), çift halkalı büyük moleküllerdir. Pirimidinler (Timin ve Sitozin) ise tek halkalı daha küçük moleküllerdir. Evrimsel süreçte mutasyonlar gerçekleşirken, bir pürinin başka bir pürine dönüşmesi (Transisyon) daha olasıdır. Bu baz ailelerinin yerleşimini izole ederek incelemek bu nedenle önemlidir.</p>",
   "problem_def": "<p>Verilen diziyi filtrelemeli; Adenin ve Guanin dışındaki karakterleri boşluk karakteriyle değiştirerek pürinlerin dizideki yapısal konumlarını göstermeliyiz.</p>",
   "matlab_logic": "<p>Bir koşulu filtrelerken birden fazla durumu kontrol etmemiz gerekiyorsa (T veya C olma durumu), Mantıksal VEYA (OR) operatörünü <code>|</code> kullanırız. Kopya bir dizi oluşturup, koşulu sağlayan noktalara hedef karakteri atamak maskeleme tekniğinin temelidir.</p>",
   "tip": "Mantıksal operatörlerde <code>||</code> (kısa devre VEYA) sadece skaler (tek değer) karşılaştırmalarda kullanılır. Vektör/dizi karşılaştırmalarında mutlaka tek çubuklu <code>|</code> kullanılmalıdır.",
   "steps": "<li>Orijinal diziyi korumak için <code>purinler</code> adlı bir kopya oluşturuyoruz.</li><li>Orijinal dizide T <strong>VEYA</strong> C olan yerlerin mantıksal maskesini (1 ve 0'lar) <code>dna == 'T' | dna == 'C'</code> ile çıkarıyoruz.</li><li>Kopya dizinin içinde, maskenin 1 olduğu indekslere ' ' (boşluk) karakterini atıyoruz.</li><li>Filtrelenmiş sonucu yazdırıyoruz.</li>"
  },
  {
   "title": "Sadece Pirimidinleri Filtreleme", "inp": "ATCGATCG", "out": " TC  TC ",
   "desc": "Dizideki pirimidinleri (C, T) koruyup, pürinleri boşluk (' ') ile değiştirin.",
   "code": "dna = 'ATCGATCG';\npirimidinler = dna;\npirimidinler(dna == 'A' | dna == 'G') = ' ';\ndisp(pirimidinler);",
   "bio": "<p>Yukarıdaki işlemin tersidir. <strong>Pirimidinler</strong> (Sitozin ve Timin) tek halkalı bazlardır. Güneşten gelen zararlı Ultraviyole (UV) ışınları, DNA üzerinde yan yana duran iki pirimidin arasına (özellikle Timin dimerleri) kovalent bağlar kurarak yapıyı bozar. Dizide yan yana pirimidinlerin (Pirimidin traktörlerinin) tespiti UV hasarına yatkın bölgelerin belirlenmesinde kullanılır.</p>",
   "problem_def": "<p>Bu kez dizide Adenin ve Guanin olan yerleri tespit edip, bu yerleri boşluk karakteriyle değiştirmeliyiz.</p>",
   "matlab_logic": "<p>Önceki pürin filtreleme sorusuyla aynı vektörel maskeleme mantığını kullanıyoruz, sadece aradığımız hedefler ('A' ve 'G') değişiyor.</p>",
   "tip": "Dizideki karakterleri değiştirmek yerine sadece konumları (indeksleri) isteseydik, <code>find(dna == 'C' | dna == 'T')</code> komutu bize pirimidinlerin sıra numaralarını tam sayı olarak verebilirdi.",
   "steps": "<li>Dizinin geçici bir kopyasını (<code>pirimidinler</code>) yaratıyoruz.</li><li>Orijinal dizide A veya G olan konumların maskesini buluyoruz.</li><li>Kopya dizinin ilgili konumlarına boşluk atayarak siliyoruz ve sadece pirimidinleri bırakıyoruz.</li>"
  }
]

# Write placeholders for 11-20
for i in range(10, 20):
    p_data.append({
        "title": f"Başlangıç Seviyesi Soru {i+1}",
        "inp": "Girdi Verisi", "out": "Çıktı Verisi",
        "desc": f"Bu, otomatik oluşturulmuş başlangıç seviyesi {i+1}. problemin açıklamasıdır.",
        "code": "% Çözüm kodunuz burada\ndisp('Sonuç');",
        "bio": "<p>Biyoinformatik analizlerde temel fonksiyonların işlevi, veriyi temizlemek ve modele hazırlamaktır. Nükleotid seviyesindeki basit istatistikler kompleks algoritmaların ilk adımıdır.</p>",
        "problem_def": "<p>Bu problemin amacı diziyi manipüle ederek istenen çıktıyı üretmektir.</p>",
        "matlab_logic": "<p>MATLAB vektörel yapısı sayesinde döngülere gerek kalmadan bu manipülasyonu gerçekleştirebilir.</p>",
        "tip": "Doğru fonksiyonu seçmek ve indekslemeyi doğru yapmak hız açısından çok önemlidir.",
        "steps": "<li>Girdiyi al.</li><li>Uygun fonksiyonu uygula.</li><li>Sonucu bastır.</li>"
    })

problems_list = []

for i, p in enumerate(p_data):
    explanation = base_exp.format(
        bio=p['bio'], 
        problem_def=p['problem_def'], 
        matlab_logic=p['matlab_logic'], 
        tip=p['tip'], 
        steps=p['steps']
    )
    
    problems_list.append({
        "id": f"b{i+1}",
        "level": "beginner",
        "title": f"{i+1}. {p['title']}",
        "description": f"<p>{p['desc']}</p><br/><p><b>Girdi:</b> <code>{p['inp']}</code></p><p><b>Beklenen Çıktı:</b> <code>{p['out']}</code></p>",
        "starter_code": "% Kodunuzu buraya yazın\n\n",
        "solution_code": p['code'],
        "expected_output": p['out'],
        "explanation": explanation
    })

# Add intermediate and advanced placeholders
for i in range(1, 21):
    problems_list.append({
        "id": f"i{i}", "level": "intermediate",
        "title": f"{i}. Orta Seviye Problem {i}",
        "description": "<p>...</p>",
        "starter_code": "", "solution_code": "", "expected_output": "", "explanation": ""
    })

for i in range(1, 11):
    problems_list.append({
        "id": f"a{i}", "level": "advanced",
        "title": f"{i}. Zor Seviye Problem {i}",
        "description": "<p>...</p>",
        "starter_code": "", "solution_code": "", "expected_output": "", "explanation": ""
    })

js_content = "const problems = " + json.dumps(problems_list, indent=2, ensure_ascii=False) + ";\n"
with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
