# coding: utf-8
import json

base_exp = """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">{bio}</div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">{problem_def}</div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">{matlab_logic}</div>
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
   "steps": "<li><code>dna = 'ATGCGTACGTCG';</code> : DNA dizisini bellekte bir karakter dizisi olarak tanımlıyoruz.</li><li><code>rna = strrep(dna, 'T', 'U');</code> : İlk parametre işlem yapılacak değişkeni, ikincisi aranacak hedefi ('T'), üçüncüsü yeni değeri ('U') temsil eder. Değişen hali <code>rna</code> değişkenine atanır.</li><li><code>disp(rna);</code> : Sonucu komut penceresinde ekrana yazdırır.</li>"
  },
  {
   "title": "GC İçeriği Hesaplama", "inp": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT", "out": "%59.09",
   "desc": "DNA dizisindeki Guanin ve Sitozin yüzdesini hesaplayın.",
   "code": "dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT';\ng = sum(dna == 'G');\nc = sum(dna == 'C');\nuzunluk = length(dna);\ngc = ((g + c) / uzunluk) * 100;\nfprintf('%%%.2f\\n', gc);",
   "bio": "<p>Çift sarmallı DNA yapısında Adenin (A) daima Timin (T) ile eşleşirken, Guanin (G) daima Sitozin (C) ile eşleşir. Termodinamik açıdan A-T eşleşmesi iki hidrojen bağı oluştururken, G-C eşleşmesi üç hidrojen bağı oluşturur. Bu biyokimyasal gerçek, G-C oranı yüksek olan DNA sarmallarının birbirinden ayrılmak için daha yüksek ısı enerjisine ihtiyaç duymasına neden olur.</p><p>Laboratuvar ortamında DNA'yı çoğaltmak için kullanılan PCR (Polimeraz Zincir Reaksiyonu) testlerinde, tasarlanan primerlerin GC içeriğinin %40 ile %60 arasında olması istenir. GC içeriğinin hesaplanması, dizinin kararlılığını ölçmenin en basit ve en yaygın yoludur.</p>",
   "problem_def": "<p>Verilen bir karakter dizisinde toplam 'G' ve 'C' karakterlerinin sayısını bulmamız, bu toplamı dizinin toplam uzunluğuna bölmemiz ve 100 ile çarparak bir yüzde değeri elde etmemiz gerekmektedir.</p>",
   "matlab_logic": "<p>MATLAB'da karakterleri saymak için mantıksal indeksleme (logical indexing) kullanılır. <code>dizi == 'Karakter'</code> ifadesi, dizinin her bir elemanını kontrol eder ve eşleşme olan yerlere 1, olmayan yerlere 0 yazar. Oluşan bu 1 ve 0'lardan oluşan matrisi <code>sum()</code> fonksiyonu ile topladığımızda frekansı buluruz.</p>",
   "tip": "Aritmetik işlemlerde parantez kullanımına dikkat edin. <code>g + c / uzunluk</code> yazmak sadece c'yi bölerken, <code>(g + c) / uzunluk</code> toplamı böler. İşlem önceliği hataları mantıksal hatalara yol açar.",
   "steps": "<li><code>g = sum(dna == 'G');</code> : Dizideki G'lerin yerini mantıksal olarak bulur ve toplayarak toplam G sayısını verir.</li><li><code>c = sum(dna == 'C');</code> : Aynı işlemi C nükleotidleri için yapar.</li><li><code>uzunluk = length(dna);</code> : Dizinin toplam karakter uzunluğunu hesaplar.</li><li><code>gc = ((g + c) / uzunluk) * 100;</code> : Oran hesaplanır ve yüzdeye çevrilir.</li><li><code>fprintf('%%%.2f\\n', gc);</code> : Sonucu virgülden sonra iki hane ile yüzde sembolü koyarak ekrana yazdırır.</li>"
  },
  {
   "title": "Nükleotid Sayımı", "inp": "AGCTTTTCATTCTGACTGCA...", "out": "A: 20, C: 12, G: 17, T: 21",
   "desc": "Dizideki A, C, G, T nükleotidlerinin sayılarını ayrı ayrı bulun.",
   "code": "dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC';\na=sum(dna=='A'); c=sum(dna=='C'); g=sum(dna=='G'); t=sum(dna=='T');\nfprintf('A: %d, C: %d, G: %d, T: %d\\n', a, c, g, t);",
   "bio": "<p>Genomların baz kompozisyonu (hangi nükleotidden ne kadar olduğu), canlı türleri arasında büyük farklılıklar gösterir. Belirli bir DNA dizisindeki dört nükleotidin mutlak sayısının bilinmesi, o dizinin istatistiksel profilini çıkarmak için ilk adımdır.</p><p>Ayrıca, baz kompozisyonundaki asimetriler (GC skew), replikasyon başlangıç noktalarının (origin of replication) tahmin edilmesinde kullanılır.</p>",
   "problem_def": "<p>DNA metin dizisini okumalı ve içindeki her bir alfabenin (A, C, G, T) ayrı ayrı frekansını (geçiş sayısını) saymalıyız. Sonunda bu dört sayıyı okunaklı bir formatta yazdırmalıyız.</p>",
   "matlab_logic": "<p>Önceki problemde kullandığımız mantıksal toplama işlemini bu kez dört farklı karakter için dört ayrı değişkende uygulayacağız. Çıktı formatı için <code>disp</code> yerine daha kontrollü olan <code>fprintf</code> fonksiyonunu kullanarak tüm sayıları tek bir satıra yerleştireceğiz.</p>",
   "tip": "Daha ileri seviyelerde, `histcounts` veya `tabulate` gibi tek geçişli istatistiksel fonksiyonlar kullanarak bu işlem büyük verilerde daha da optimize edilebilir.",
   "steps": "<li><code>a=sum(dna=='A');</code> : A nükleotidlerini sayar.</li><li>Aynı işlem C, G ve T için de sırasıyla tekrarlanarak <code>c</code>, <code>g</code>, ve <code>t</code> değişkenleri oluşturulur.</li><li><code>fprintf</code> içindeki <code>%d</code> yer tutucularına tam sayılar sırasıyla yerleştirilerek ekrana basılır.</li>"
  },
  {
   "title": "DNA Uzunluğunu Bulma", "inp": "ATCGATCGATCG", "out": "12",
   "desc": "Verilen DNA dizisinin nükleotid bazındaki toplam uzunluğunu ekrana yazdırın.",
   "code": "dna = 'ATCGATCGATCG';\ndisp(length(dna));",
   "bio": "<p>Bir genin veya kromozomun uzunluğu, biyolojide genellikle Baz Çifti (Base Pair - bp) cinsiyle ifade edilir. Örneğin insan genomu yaklaşık 3.2 milyar baz çiftinden oluşurken, basit bir virüs genomu birkaç bin baz çiftinden oluşabilir. Uzunluk verisi, analiz sırasında bellek gereksinimlerini hesaplamakta kullanılır.</p>",
   "problem_def": "<p>Sadece dizideki toplam karakter sayısını saymamız gerekmektedir. Uzunluk tam sayı bir değer olarak geri dönmelidir.</p>",
   "matlab_logic": "<p>MATLAB bir metin dizisini tek boyutlu bir karakter dizisi olarak görür. Vektörlerin en büyük boyutunun uzunluğunu bulmak için <code>length()</code> fonksiyonu standarttır.</p>",
   "tip": "Eğer diziniz çok boyutlu bir matris veya string array ise, <code>length</code> yanıltıcı olabilir; böyle durumlarda <code>strlength</code> veya <code>size</code> kullanmak daha güvenlidir.",
   "steps": "<li><code>length(dna)</code> : Karakter sayısını elde eder.</li><li>Değeri <code>disp()</code> ile ekrana yazdırırız.</li>"
  },
  {
   "title": "Ters Çevrilmiş DNA Dizisi", "inp": "ATGC", "out": "CGTA",
   "desc": "DNA dizisini sondan başa doğru (ters olarak) okuyan bir kod yazın.",
   "code": "dna = 'ATGC';\nters = reverse(dna);\ndisp(ters);",
   "bio": "<p>DNA sarmalının yönlülüğü vardır; moleküler olarak 5' ucundan 3' ucuna doğru uzanır. Gen dizilim (sekanslama) teknolojilerinde, cihaz bazen DNA'yı beklenen yönde değil, ters yönde okuyabilir. Bu ters okumaları düzeltebilmek veya diziyi tersten analiz etmek biyoinformatik ön işlemlerinin parçasıdır.</p>",
   "problem_def": "<p>Karakter dizisinin sıralamasını tam tersine çevirerek (son harfi ilk harf yaparak) yeni bir dizi oluşturmalıyız.</p>",
   "matlab_logic": "<p>MATLAB 2016b ve sonrası sürümlerde karakter ve metin işlemleri için <code>reverse()</code> fonksiyonu eklenmiştir. Eski sürümlerde ise vektör indeksleme kullanılarak <code>dizi(end:-1:1)</code> şeklinde çözüm üretilirdi.</p>",
   "tip": "Matris indeksleme <code>(end:-1:1)</code> yöntemi, sadece metinlerde değil her türlü sayısal vektörü ters çevirmekte de kullanabileceğiniz çok güçlü bir araçtır.",
   "steps": "<li><code>reverse(dna)</code> : Dizinin ayna görüntüsünü (tersini) alır. Alternatif olarak <code>dna(end:-1:1)</code> de kullanılabilirdi.</li><li>Sonuç ekrana basılır.</li>"
  },
  {
   "title": "Ters Tamamlayıcı (Reverse Complement)", "inp": "AAAACCCGGT", "out": "ACCGGGTTTT",
   "desc": "Bir DNA dizisinin ters tamamlayıcısını (A->T, C->G yapıp tersine çevirme) bulun.",
   "code": "dna = 'AAAACCCGGT';\nt = dna;\nt(dna=='A')='T';\nt(dna=='T')='A';\nt(dna=='C')='G';\nt(dna=='G')='C';\nters_tamamlayici = t(end:-1:1);\ndisp(ters_tamamlayici);",
   "bio": "<p>Çift iplikli DNA'da bir iplik 5' → 3' yönünde ilerlerken, karşı iplik ona antiparalel olarak 3' → 5' yönünde ilerler. Veritabanlarında genellikle sadece tek bir iplik saklanır. Diğer ipliğin dizilimini bulmak için mevcut dizinin önce tamamlayıcısı alınır, sonra antiparalel yönlülükten dolayı dizi tersine çevrilir. Bu işleme <strong>Reverse Complement</strong> denir ve primer tasarımı algoritmalarında sürekli kullanılır.</p>",
   "problem_def": "<p>Önce her bir harfi biyolojik eşleniğine dönüştürmeli, sonrasında elde edilen diziyi sondan başa doğru ters çevirmeliyiz.</p>",
   "matlab_logic": "<p>Eğer <code>strrep</code> kullansaydık, A'ları T yaptıktan sonra, T'leri A yapmaya çalıştığımızda karışıklık yaşardık. Bu yüzden orijinal diziyi bir maske (referans) olarak kullanıp, geçici kopya dizi üzerinde atamalar yapmak en güvenilir algoritmadır.</p>",
   "tip": "MATLAB'ın Bioinformatics Toolbox eklentisinde bu işlemi tek komutla yapan <code>seqrcomplement()</code> fonksiyonu vardır, ancak algoritma mantığını oturtmak için kendimiz yazmak en doğrusudur.",
   "steps": "<li><code>t = dna;</code> : Üzerinde değişiklik yapacağımız kopyayı oluştururuz.</li><li><code>t(dna=='A') = 'T';</code> : Orijinal dizide 'A' olan indekslere kopya dizide 'T' yazarız.</li><li>Aynı işlemi tüm eşleşmeler (A-T, C-G) için tekrarlarız.</li><li><code>t(end:-1:1)</code> ile elde ettiğimiz diziyi tersine çevirip yazdırırız.</li>"
  },
  {
   "title": "RNA'dan DNA'ya Ters Transkripsiyon", "inp": "AUGGCUACUUAA", "out": "ATGGCTACTTAA",
   "desc": "RNA dizisini tekrar DNA'ya çeviren (U -> T) bir kod yazın.",
   "code": "rna = 'AUGGCUACUUAA';\ndna = strrep(rna, 'U', 'T');\ndisp(dna);",
   "bio": "<p>Normal şartlarda bilgi akışı DNA'dan RNA'ya doğrudur. Ancak Retrovirüsler (örneğin HIV), <strong>Ters Transkriptaz</strong> adlı enzimlerini kullanarak kendi RNA'larından DNA sentezlerler. Biyoinformatikte RNA tabanlı verileri DNA veritabanlarıyla karşılaştırmak için yazılımsal olarak ters transkripsiyon yaparız.</p>",
   "problem_def": "<p>Verilen RNA metin dizisindeki tüm 'U' karakterlerini bularak onları 'T' karakteri ile değiştirmeliyiz.</p>",
   "matlab_logic": "<p>İlk problemin (Transkripsiyon) tam tersidir. Hedef ve yeni değer parametrelerinin yerini değiştirerek <code>strrep</code> fonksiyonunu kullanmak yeterlidir.</p>",
   "tip": "Metin tabanlı veri setlerinde (FASTA vb.) bu basit dönüşümler, hizalama (alignment) algoritmalarından hemen önce yapılan veri temizleme işlemidir.",
   "steps": "<li><code>strrep</code> fonksiyonu ile 'U' aranıp yerine 'T' koyulur.</li><li>Elde edilen cDNA dizisi ekrana basılır.</li>"
  },
  {
   "title": "Motif Arama", "inp": "GATATATGCATATACTT (aranan: ATGC)", "out": "8",
   "desc": "Büyük bir dizi içinde belirli bir motifin başladığı indeksi bulun.",
   "code": "dna = 'GATATATGCATATACTT';\nindeks = strfind(dna, 'ATGC');\ndisp(indeks);",
   "bio": "<p>Genlerin ifade edilip edilmemesini kontrol eden düzenleyici proteinler, DNA üzerinde rastgele yerlere değil, belirli kısa şifrelere bağlanırlar. Bu kısa anlamlı dizilere <strong>Motif</strong> denir (Örn: TATA Box). Bir gen bölgesinde bu motiflerin nerede başladığını bulmak, gen regülasyonunu anlamanın anahtarıdır.</p>",
   "problem_def": "<p>Büyük bir ana karakter dizisinin içinde, verilen alt dizinin (substring) nerede bulunduğunu (başlangıç konumunu) bulmamız gerekmektedir.</p>",
   "matlab_logic": "<p>Metin içinde alt metin aramak için MATLAB'ın standart komutu <code>strfind</code>'dir. Bu fonksiyon, motif birden fazla yerde geçiyorsa, tüm başlangıç indekslerini bir vektör olarak döndürür.</p>",
   "tip": "Eğer motif dizinin içinde hiç geçmiyorsa, <code>strfind</code> boş bir vektör <code>[]</code> döndürür. İleri düzey kodlamada bunu <code>isempty()</code> ile yakalamak iyi bir pratiktir.",
   "steps": "<li><code>strfind(dna, 'ATGC')</code> komutu ile motifin dizide geçtiği tüm koordinatlar bulunur.</li><li>İndeks değeri ekrana yazdırılır.</li>"
  },
  {
   "title": "Sadece Pürinleri Filtreleme", "inp": "ATCGATCG", "out": "A G A G",
   "desc": "Dizideki pürinleri (A, G) koruyup, pirimidinleri boşluk (' ') ile değiştirin.",
   "code": "dna = 'ATCGATCG';\npurinler = dna;\npurinler(dna == 'T' | dna == 'C') = ' ';\ndisp(purinler);",
   "bio": "<p>DNA'yı oluşturan bazlar kimyasal yapılarına göre iki aileye ayrılır. <strong>Pürinler</strong> (Adenin ve Guanin), çift halkalı büyük moleküllerdir. Evrimsel süreçte bir pürinin başka bir pürine dönüşmesi (Transisyon) daha olasıdır. Pürinlerin yerleşimini izole ederek incelemek yapısal analiz için önemlidir.</p>",
   "problem_def": "<p>Diziyi filtrelemeli; Adenin ve Guanin dışındaki karakterleri boşluk karakteriyle değiştirerek pürinlerin yapısal konumlarını göstermeliyiz.</p>",
   "matlab_logic": "<p>Bir koşulu filtrelerken birden fazla durumu kontrol etmemiz gerekiyorsa, Mantıksal VEYA (OR) operatörünü <code>|</code> kullanırız. Kopya bir dizi oluşturup, koşulu sağlayan noktalara hedef karakteri atamak temel maskeleme tekniğidir.</p>",
   "tip": "Mantıksal operatörlerde <code>||</code> (kısa devre VEYA) skaler işlemlerde kullanılır. Vektör karşılaştırmalarında mutlaka tek çubuklu <code>|</code> kullanılmalıdır.",
   "steps": "<li><code>purinler</code> adlı kopya bir dizi oluşturulur.</li><li><code>dna == 'T' | dna == 'C'</code> ile pirimidin olan yerlerin maskesi çıkarılır.</li><li>Kopya dizide bu maskeye uyan yerlere ' ' atanarak temizlenir.</li>"
  },
  {
   "title": "Sadece Pirimidinleri Filtreleme", "inp": "ATCGATCG", "out": " TC  TC ",
   "desc": "Dizideki pirimidinleri (C, T) koruyup, pürinleri boşluk (' ') ile değiştirin.",
   "code": "dna = 'ATCGATCG';\npirimidinler = dna;\npirimidinler(dna == 'A' | dna == 'G') = ' ';\ndisp(pirimidinler);",
   "bio": "<p><strong>Pirimidinler</strong> (Sitozin ve Timin) tek halkalı bazlardır. Güneşten gelen Ultraviyole (UV) ışınları, DNA üzerinde yan yana duran iki pirimidin arasına (Timin dimerleri) zararlı kovalent bağlar kurabilir. Dizide yan yana pirimidinlerin (Pirimidin traktörlerinin) tespiti UV hasarına yatkın bölgelerin belirlenmesinde kullanılır.</p>",
   "problem_def": "<p>Bu kez dizide Adenin ve Guanin olan yerleri tespit edip, bu yerleri boşluk karakteriyle değiştirmeliyiz.</p>",
   "matlab_logic": "<p>Pürin filtreleme sorusuyla aynı vektörel maskeleme mantığını kullanıyoruz, sadece aradığımız hedefler ('A' ve 'G') değişmektedir.</p>",
   "tip": "Karakter değiştirmek yerine sadece indeksleri isteseydik, <code>find()</code> fonksiyonu kullanarak pirimidinlerin sıra numaralarını alabilirdik.",
   "steps": "<li>Geçici bir kopya oluşturulur.</li><li>A veya G olan konumların maskesi bulunur.</li><li>Bu konumlara boşluk atanarak sadece pirimidinler geride bırakılır.</li>"
  },
  {
   "title": "Mutasyon (Hamming Mesafesi) Hesaplama", "inp": "GAGCCT, CATCGT", "out": "7",
   "desc": "Eşit uzunluktaki iki diziyi karşılaştırıp farklı nükleotid sayılarını bulun.",
   "code": "d1='GAGCCTACTAACGGGAT'; d2='CATCGTAATGACGGCCT';\nfark = sum(d1 ~= d2);\ndisp(fark);",
   "bio": "<p>Evrimsel süreçte organizmaların genetik kodlarında kopyalama hatalarına bağlı olarak mutasyonlar meydana gelir. Aynı atadan geldiği varsayılan iki homolog diziyi yan yana koyup farklı olan nükleotidleri saymak, o iki türün evrimsel olarak birbirinden ne kadar uzaklaştığını gösteren (Moleküler Saat) temel bir filogenetik analizdir. Bu sayısal farklılığa bilgisayar biliminde Hamming Mesafesi denir.</p>",
   "problem_def": "<p>Girdi olarak alınan aynı uzunluktaki iki dizinin her bir indeksini karşılıklı olarak kontrol etmemiz ve birbirine eşit olmayan karakter çiftlerinin sayısını toplamamız gerekmektedir.</p>",
   "matlab_logic": "<p>MATLAB'da iki vektörü eleman eleman (element-wise) karşılaştırmak çok basittir. Eşit değil (<code>~=</code>) operatörü iki diziyi alır ve karakterlerin farklı olduğu her nokta için 1, aynı olduğu noktalar için 0 içeren mantıksal bir dizi döndürür. Sonra bu vektördeki 1'ler toplanır.</p>",
   "tip": "Dizilerin uzunlukları birbirine eşit değilse MATLAB hata verecektir. Gerçek analizlerde diziler önce hizalanır (Alignment), aralara boşluklar (gap) eklenerek eşit uzunluğa getirilir, ardından bu metrik hesaplanır.",
   "steps": "<li>İki dizi aynı uzunlukta belleğe alınır.</li><li><code>d1 ~= d2</code> komutuyla diziler birbiriyle üst üste çakıştırılarak farklı olan lokasyonlar tespit edilir.</li><li><code>sum()</code> fonksiyonu bu farklı lokasyonların adedini hesaplayıp <code>fark</code> değişkenine atar.</li><li>Toplam mutasyon sayısı ekrana basılır.</li>"
  },
  {
   "title": "Dizi Ligasayonu (Birleştirme)", "inp": "ATGC, GTAC", "out": "ATGCGTAC",
   "desc": "İki farklı DNA parçasını birbirine bağlayan bir kod yazın.",
   "code": "p1='ATGC'; p2='GTAC';\nbirlesik=[p1, p2];\ndisp(birlesik);",
   "bio": "<p>Rekombinant DNA teknolojisinde (genetik mühendisliği), farklı canlılara ait genler veya DNA parçaları laboratuvar ortamında kesilip biçilir. Kesilen bu parçaları birbirine yapıştıran hücresel enzimlere <strong>Ligaz</strong> enzimi denir. İki farklı veri setinden gelen parçaların birleştirilmesi işlemi, bu biyolojik ligasyonun yazılımdaki tam karşılığıdır.</p>",
   "problem_def": "<p>İki ayrı string dizisini ardışık (uç uca) olarak birleştirerek tek bir uzun dizi elde etmeliyiz.</p>",
   "matlab_logic": "<p>MATLAB'da stringleri birleştirmenin en basit ve temiz yolu, vektör birleştirme köşeli parantezlerini <code>[]</code> kullanmaktır. Stringler karakter dizisi olduğu için yatay birleştirmede yan yana dizilirler. Alternatif olarak <code>strcat(p1, p2)</code> fonksiyonu da kullanılabilir.</p>",
   "tip": "Çok sayıda uzun diziyi birleştiriyorsanız bellek tahsisi (pre-allocation) önem kazanır, ancak kısa işlemler için köşeli parantez yeterlidir.",
   "steps": "<li>İki dizi değişkenlere atanır.</li><li><code>[p1, p2]</code> yapısı kullanılarak iki dizi tek bir matris (satır vektörü) içinde birleştirilir.</li><li>Yeni uzun dizi ekrana basılır.</li>"
  },
  {
   "title": "Nükleotid Standartlaştırma", "inp": "atgCgtA", "out": "ATGCGTA",
   "desc": "Dizideki tüm nükleotidleri büyük harfe çeviren bir kod yazın.",
   "code": "dna = 'atgCgtA';\ndisp(upper(dna));",
   "bio": "<p>Biyoinformatik veritabanlarından (GenBank, FASTA formatlı dosyalar) çekilen sekanslar, veriyi yükleyen merkeze göre farklı formatlarda olabilir. Bazen gen bölgeleri büyük harfle, kodlanmayan intron bölgeleri küçük harfle ifade edilir. Algoritmalar genellikle büyük/küçük harfe duyarlıdır, bu yüzden analiz öncesi verinin standartlaştırılması ve temizlenmesi zorunludur.</p>",
   "problem_def": "<p>Metin dizisinde bulunan tüm harflerin kontrol edilmesi ve eğer küçük harf ise büyük harf karşılığına dönüştürülmesi gerekmektedir.</p>",
   "matlab_logic": "<p>MATLAB metin işleme standart fonksiyonlarından <code>upper()</code>, dizi içindeki tüm harfleri İngilizce alfabe standartlarına göre büyük harfe çevirir. Halihazırda büyük olanlara dokunmaz.</p>",
   "tip": "Biyoinformatik boru hatlarında (pipeline), veritabanından veri okunur okunmaz uygulanması gereken ilk adım genellikle <code>upper()</code> veya <code>strtrim()</code> (boşlukları silme) fonksiyonlarıdır.",
   "steps": "<li>Karmaşık formatlı dizi tanımlanır.</li><li><code>upper(dna)</code> fonksiyonu kullanılarak tam standartlaştırma sağlanır.</li><li>Temizlenmiş dizi ekrana yazdırılır.</li>"
  },
  {
   "title": "Bilinmeyen Nükleotidleri Sayma", "inp": "ATGNNNCGATN", "out": "4",
   "desc": "Dizideki toplam okunamayan 'N' sayısını bulan bir kod yazın.",
   "code": "dna = 'ATGNNNCGATN';\ndisp(sum(dna == 'N'));",
   "bio": "<p>Modern DNA sekanslama cihazları (Yeni Nesil Sekanslama - NGS), her bir nükleotidi florasan sinyaller okuyarak belirler. Eğer okuma sırasında sinyal çok zayıfsa veya cihaz o pozisyonda hangi nükleotid olduğundan emin olamazsa, o noktaya A, C, G veya T yerine <strong>N (Any Nucleotide - Bilinmeyen)</strong> yazar. Bir dizideki N oranının yüksekliği, o genetik verinin kalitesinin düşük olduğunu gösterir ve analiz öncesi filtrelenmesi gerekebilir.</p>",
   "problem_def": "<p>Dizi içinde geçen 'N' karakterlerinin mutlak sayısını bulmalıyız.</p>",
   "matlab_logic": "<p>Önceki nükleotid sayma problemlerinde olduğu gibi, belirli bir hedef karakteri saymak için mantıksal maske oluşturmak ve <code>sum()</code> komutuyla bu maskeyi toplamak en etkili yoldur.</p>",
   "tip": "Eğer dizideki N oranı %5'in üzerindeyse, genelde o sekans dosyası (FASTQ/FASTA) güvenilmez kabul edilip analiz dışı bırakılır.",
   "steps": "<li><code>dna == 'N'</code> ile sadece N harflerinin olduğu yerler 1 yapılır.</li><li><code>sum()</code> ile bu 1'lerin toplamı alınarak frekans elde edilir.</li>"
  },
  {
   "title": "Başlangıç Kodonunu Kontrol Etme", "inp": "ATGCGTACG", "out": "1",
   "desc": "Dizinin başlangıç kodonu olan 'ATG' ile başlayıp başlamadığını kontrol edin.",
   "code": "dna = 'ATGCGTACG';\ndisp(startsWith(dna, 'ATG'));",
   "bio": "<p>Hücrede protein sentezinin (Translasyon) başlaması için ribozomun mRNA üzerinde bir başlangıç sinyali bulması gerekir. Bu sinyal istisnasız olarak <strong>Metiyonin</strong> amino asidini kodlayan <strong>ATG</strong> (RNA'da AUG) kodonudur. Biyoinformatik açık okuma çerçevesi (Open Reading Frame - ORF) bulma algoritmaları, proteini kodlayan genetik kodun nerede başladığını bulmak için her zaman önce bu kodonu arar.</p>",
   "problem_def": "<p>Verilen dizinin ilk 3 karakterinin tam olarak 'A', 'T', 'G' dizilimine eşit olup olmadığını belirten bir mantıksal değer (1 veya 0) üretmeliyiz.</p>",
   "matlab_logic": "<p>Modern MATLAB versiyonlarında bir string'in belirli bir dizi ile başlayıp başlamadığını anlamanın en pratik yolu <code>startsWith()</code> fonksiyonudur. Eğer eski bir versiyon kullanılıyorsa, <code>strncmp(dna, 'ATG', 3)</code> veya <code>dna(1:3) == 'ATG'</code> alternatifleri kullanılabilir.</p>",
   "tip": "Başlangıç kodonu analizi sadece ilk indekste değil, dizinin ortalarında da yapılabilir. Buna ORF tespiti denir ve ileri seviye bir işlemdir.",
   "steps": "<li><code>startsWith(dna, 'ATG')</code> fonksiyonuna dizi ve hedef kodon verilir.</li><li>Dönen mantıksal değer (true/false) doğrudan ekrana yazdırılır.</li>"
  },
  {
   "title": "Bitiş Kodonunu Kontrol Etme", "inp": "ATGCGTTAA", "out": "1",
   "desc": "Dizinin bitiş kodonlarından biriyle (TAA, TAG veya TGA) bitip bitmediğini kontrol edin.",
   "code": "dna = 'ATGCGTTAA';\ndisp(endsWith(dna, 'TAA') | endsWith(dna, 'TAG') | endsWith(dna, 'TGA'));",
   "bio": "<p>Ribozom, mRNA üzerinde üçlü nükleotid bloklarını (kodonları) okuyarak protein zincirini uzatır. Sentezin durması gerektiğini ise <strong>Dur (Stop) Kodonları</strong> denilen üç özel sekans söyler: TAA (Ochre), TAG (Amber) ve TGA (Opal). Dizinin bu kodonlardan biriyle bitmesi, geçerli bir gen dizisi ile karşı karşıya olma ihtimalimizi artırır.</p>",
   "problem_def": "<p>Dizinin son 3 karakterini alıp, bunun üç ihtimalden herhangi birine eşit olup olmadığını test etmeli ve tek bir mantıksal sonuç döndürmeliyiz.</p>",
   "matlab_logic": "<p>Sonu kontrol etmek için <code>endsWith()</code> kullanılır. 3 farklı senaryomuz olduğu için, bu üç ihtimali Mantıksal VEYA operatörü (<code>|</code>) ile zincirleme bağlarız. Eğer şartlardan sadece biri doğruysa, toplam sonuç doğru (1) çıkacaktır.</p>",
   "tip": "Mantıksal operatörleri zincirlerken okunabilirliği artırmak için parantezleri doğru konumlandırmak hayat kurtarıcı olabilir.",
   "steps": "<li>TAA için <code>endsWith()</code> kontrolü yapılır.</li><li>TAG için ve TGA için kontroller yapılır.</li><li>Bu üç kontrol VEYA (<code>|</code>) ile birleştirilir ve sonuç yazdırılır.</li>"
  },
  {
   "title": "Nükleotid Konumu", "inp": "ATGCG", "out": "G",
   "desc": "Bir DNA dizisinin tam ortasındaki (merkezindeki) nükleotidi bulun.",
   "code": "dna = 'ATGCG';\norta = ceil(length(dna) / 2);\ndisp(dna(orta));",
   "bio": "<p>Biyoinformatikte dizileri incelerken bazen tüm diziyi değil, sadece hareketli bir pencere (sliding window) içindeki bölgeyi analiz ederiz. Bu tür bölgesel istatistik algoritmalarında, analiz edilen parçanın merkez noktasını (pivot) belirlemek, ağırlık hesaplamaları için çok önemlidir.</p>",
   "problem_def": "<p>Dizinin toplam uzunluğunun yarısına denk gelen (tek sayı ise yukarı/aşağı yuvarlanmış) indeks numarasını bulup, o numaradaki harfi geri döndürmeliyiz.</p>",
   "matlab_logic": "<p>MATLAB indeksleri 1'den başlar (Python veya C gibi 0'dan değil). Uzunluk ikiye bölündüğünde 5/2 = 2.5 çıkarsa, bu indeks kullanılamaz. <code>ceil()</code> fonksiyonu bu ondalıklı sayıyı yukarı tam sayıya yuvarlayarak bize net bir indeks noktası verir.</p>",
   "tip": "Tam sayı yuvarlaması için <code>round()</code> veya <code>floor()</code> da kullanılabilir; hangi algoritma standardının istendiğine göre karar verilir.",
   "steps": "<li><code>length(dna) / 2</code> ile orta değer bulunur.</li><li><code>ceil()</code> fonksiyonu ile çıkan sayı tam sayıya yuvarlanıp <code>orta</code> değişkenine atanır.</li><li><code>dna(orta)</code> şeklinde parantez indekslemesi yapılarak harf çağırılır.</li>"
  },
  {
   "title": "Alt Dizi (Subsequence) Çıkarma", "inp": "ATGCGTACGTCG", "out": "GCGTA",
   "desc": "Dizinin 3. nükleotidinden başlayıp 7. nükleotidi dahil olan aralığı çıkarın.",
   "code": "dna = 'ATGCGTACGTCG';\ndisp(dna(3:7));",
   "bio": "<p>Genomik veritabanlarında arama yaparken (örneğin BLAST algoritması), bütün bir genom yerine sadece tespit edilen bir gen bölgesinin veya ekson parçasının izole edilmesi gerekir. Diziyi dilimlere ayırmak (slicing), genomik işlemlerin en temel araçlarından biridir.</p>",
   "problem_def": "<p>Ana karakter dizisinden belli bir başlangıç (3) ve bitiş (7) noktası arasındaki harfleri yeni bir dizi olarak ayırmalıyız.</p>",
   "matlab_logic": "<p>MATLAB'da iki nokta üst üste (<code>:</code>) operatörü, indeks aralığı belirlemek için kullanılır. <code>dizi(baslangic:bitis)</code> mantığı ile vektörün veya metnin içindeki o bölüm dilimlenerek dışarı alınır.</p>",
   "tip": "Sondan 3 karakteri almak isterseniz <code>dizi(end-2:end)</code> yazımını kullanabilirsiniz. <code>end</code> anahtar kelimesi dilimleme işlemlerinde çok kullanışlıdır.",
   "steps": "<li>Parantez içinde başlangıç ve bitiş indeksleri arasına iki nokta üst üste konularak aralık belirtilir: <code>(3:7)</code>.</li><li>Dilimlenen bu alt dizi doğrudan komut satırına bastırılır.</li>"
  },
  {
   "title": "Polindromik DNA Dizisi", "inp": "GCGC", "out": "1",
   "desc": "Dizinin palindromik (kendi tersi ile aynı) olup olmadığını kontrol edin.",
   "code": "dna = 'GCGC';\nters = dna(end:-1:1);\ndisp(strcmp(dna, ters));",
   "bio": "<p>Palindromik kelimeler tersten okunduğunda da aynı olan kelimelerdir (KABAK gibi). Biyolojide palindromik diziler çok özel bir öneme sahiptir; çünkü Restriksiyon Enzimleri (moleküler makaslar) DNA'yı bu bölgelerden tanır ve keser. Örneğin meşhur EcoRI enzimi GAATTC dizisini arar (ve bu dizi diğer iplikte tersten GAATTC okunduğu için palindromik bir bölge oluşturur).</p>",
   "problem_def": "<p>Dizinin ters halini oluşturmalı ve bu ters halin orijinal dizi ile karakter karakter tam olarak aynı olup olmadığını (eşitliğini) mantıksal olarak döndürmeliyiz.</p>",
   "matlab_logic": "<p>Karakter dizilerinin içeriğinin tam olarak eşit olup olmadığını anlamak için MATLAB'da <code>==</code> kullanmak risklidir, çünkü boyutları farklıysa hata verir. Karakter dizilerini karşılaştırmanın en güvenli yolu <code>strcmp()</code> (String Compare) fonksiyonudur.</p>",
   "tip": "Büyük-küçük harf duyarlılığını ortadan kaldırmak isterseniz <code>strcmpi()</code> (i = ignore case) kullanabilirsiniz.",
   "steps": "<li><code>dna(end:-1:1)</code> kullanılarak dizinin tersten dizilmiş bir kopyası oluşturulur.</li><li><code>strcmp(dna, ters)</code> kullanılarak iki dizinin kimliği doğrulanır.</li><li>Eşitse 1 (true), değilse 0 (false) döner.</li>"
  },
  {
   "title": "Motif Frekansı", "inp": "CGCGCGCG", "out": "4",
   "desc": "Belirli bir dinükleotidin ('CG') toplam kaç kez geçtiğini sayın.",
   "code": "dna = 'CGCGCGCG';\nindeksler = strfind(dna, 'CG');\ndisp(length(indeksler));",
   "bio": "<p>İnsan genomunda Sitozin(C) ve Guanin(G) nükleotidlerinin yan yana geldiği durumlara (CpG bölgeleri) sıklıkla rastlanır. Bu bölgeler, hücre tarafından Metilasyon adı verilen epigenetik bir yöntemle modifiye edilebilir. Bir gen bölgesinde CpG dinükleotidinin yoğunluğu yüksekse (CpG Adacığı), o genin ifadesinin (çalışıp çalışmamasının) epigenetik kontrol altında olma ihtimali çok yüksektir.</p>",
   "problem_def": "<p>Sadece tek bir harfi değil, iki veya daha uzun harften oluşan bir blok şifrenin dizide kaç kez tekrar ettiğini bulmalıyız.</p>",
   "matlab_logic": "<p>Daha önceki Motif Arama probleminde kullandığımız <code>strfind()</code> bize bulunan motiflerin başlangıç lokasyonlarından oluşan bir vektör veriyordu. Bu lokasyonların sayısı, yani <code>strfind</code>'dan dönen vektörün eleman uzunluğu (length), doğrudan o motifin frekansıdır.</p>",
   "tip": "Dönen indeks vektörünün uzunluğu, motifin kaç kez geçtiğine eşittir. Bu iki güçlü fonksiyonun (length ve strfind) iç içe kullanımı yaygın bir desendir.",
   "steps": "<li><code>strfind(dna, 'CG')</code> ile hedef dinükleotidin konum vektörü elde edilir.</li><li>Elde edilen vektörün <code>length()</code> komutuyla toplam eleman sayısı bulunur ve yazdırılır.</li>"
  }
]

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
        "description": "<p>Orta seviye sorular eklenecektir.</p>",
        "starter_code": "% Kodunuzu buraya yazın\n", "solution_code": "disp('Hazırlanıyor...');", "expected_output": "Hazırlanıyor...", "explanation": "Orta seviye soru açıklaması eklenecektir."
    })

for i in range(1, 11):
    problems_list.append({
        "id": f"a{i}", "level": "advanced",
        "title": f"{i}. Zor Seviye Problem {i}",
        "description": "<p>Zor seviye sorular eklenecektir.</p>",
        "starter_code": "% Kodunuzu buraya yazın\n", "solution_code": "disp('Hazırlanıyor...');", "expected_output": "Hazırlanıyor...", "explanation": "Zor seviye soru açıklaması eklenecektir."
    })

js_content = "const problems = " + json.dumps(problems_list, indent=2, ensure_ascii=False) + ";\n"
with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
