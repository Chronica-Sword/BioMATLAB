# coding: utf-8
import json

base_exp = """
    <h4>Biyolojik Arka Plan</h4>
    <p>{bio}</p>
    <div class="highlight-box">
        <strong>💡 MATLAB Yaklaşımı:</strong><br>
        {matlab}
    </div>
    <h4>Çözüm Adımları</h4>
    <ol>
        {steps}
    </ol>
"""

p_data = [
  ("DNA'dan RNA'ya Transkripsiyon", "ATGCGTACGTCG", "AUGCGUACGUCG", 
   "DNA'da Timin (T) nükleotidi, RNA'da Urasil (U) ile yer değiştirir.", 
   "dna = 'ATGCGTACGTCG';\nrna = strrep(dna, 'T', 'U');\ndisp(rna);",
   "Transkripsiyon, DNA'daki bilginin mesajcı RNA'ya (mRNA) kopyalanması sürecidir. Bu süreçte RNA polimeraz enzimi, DNA şablonunu okuyarak RNA zincirini sentezler. En büyük kimyasal fark, RNA'da Timin yerine Urasil bulunmasıdır.",
   "Karakter dizilerinde yer değiştirme işlemi için `strrep(orijinal, eski_parca, yeni_parca)` fonksiyonu kullanılır. Bu vektörel fonksiyon tüm 'T'leri tek seferde 'U' yapar.",
   "<li>DNA dizisini bir string değişkene atayın.</li><li><code>strrep</code> kullanarak 'T' harflerini 'U' ile değiştirin.</li><li>Çıkan RNA sonucunu ekrana yazdırın.</li>"),
   
  ("GC İçeriği Hesaplama", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCT", "%59.09",
   "Bir DNA dizisindeki Guanin (G) ve Sitozin (C) nükleotidlerinin toplam yüzdesini hesaplayan kod yazın.",
   "dna = 'CCACCCTCGTGGTATGGCT...';\ng = sum(dna == 'G'); c = sum(dna == 'C');\ngc_yuzdesi = ((g + c) / length(dna)) * 100;\nfprintf('%%%.2f\\n', gc_yuzdesi);",
   "Guanin ve Sitozin arasında 3 hidrojen bağı varken, Adenin ve Timin arasında 2 bağ bulunur. GC içeriği yüksek olan DNA sarmalları ısıya daha dayanıklıdır ve erime sıcaklıkları (Tm) yüksektir. Biyoinformatikte primer tasarımı için kritik bir metrik hesaplamasıdır.",
   "Dizideki belirli karakterleri saymak için `sum(dizi == 'Karakter')` şeklindeki mantıksal (logical) indekslemeyi kullanmak döngülerden çok daha hızlıdır.",
   "<li>`==` operatörü ile G'lerin yerlerini mantıksal 1'ler olarak bulun ve `sum` ile toplayın.</li><li>Aynı işlemi C nükleotidleri için yapın.</li><li>G ve C toplamını dizinin toplam uzunluğuna (`length`) bölün ve 100 ile çarpın.</li>"),

  ("Nükleotid Sayımı", "AGCTTTTCATTCTGACTGCA...", "A: 20, C: 12, G: 17, T: 21",
   "Verilen bir DNA dizisindeki her bir nükleotidin (A, C, G, T) sayısını bulup yazdırın.",
   "dna = 'AGCT...';\na=sum(dna=='A'); c=sum(dna=='C'); g=sum(dna=='G'); t=sum(dna=='T');\nfprintf('A:%d, C:%d, G:%d, T:%d\\n', a, c, g, t);",
   "Genomik dizilerin bileşimini (composition) anlamak, o bölgenin gen kodlayıp kodlamadığını (örneğin CpG adacıkları) belirlemek için temel bir istatistiksel analizdir.",
   "Ayrı ayrı `sum()` işlemi yapılabileceği gibi, MATLAB'ın `histcounts` veya kategorik dizi özellikleri de kullanılabilir. Temel seviye için mantıksal toplama idealdir.",
   "<li>A nükleotidi için `sum(dna == 'A')` ile sayım yapın.</li><li>C, G ve T için de aynı mantığı tekrarlayın.</li><li>Tüm sayıları `fprintf` kullanarak formatlı bir şekilde ekrana yazdırın.</li>"),

  ("DNA Uzunluğunu Bulma", "ATCGATCGATCG", "12",
   "Verilen bir DNA dizisinin toplam uzunluğunu ekrana yazdırın.",
   "dna = 'ATCGATCGATCG';\ndisp(length(dna));",
   "Bir dizinin toplam nükleotid sayısı (baz çifti - bp), genom haritalama ve sekanslama kalitesini ölçme süreçlerinin ilk ve en basit adımıdır.",
   "Karakter dizilerinin karakter sayısını almak için `length` fonksiyonu kullanılır. Boyut vektörü almak içinse `size` kullanılır.",
   "<li>`length(dna)` fonksiyonunu çağırarak dizinin uzunluğunu elde edin.</li><li>Elde ettiğiniz tam sayı değerini `disp` ile ekrana yazdırın.</li>"),

  ("Ters Çevrilmiş DNA Dizisi", "ATGC", "CGTA",
   "DNA dizisini sondan başa doğru (ters olarak) okuyan bir kod yazın.",
   "dna = 'ATGC';\nters = reverse(dna);\ndisp(ters);",
   "Sıralamaları tersine çevirmek, DNA sarmalının yönlülüğünü (5' -> 3' veya tam tersi) anlamak ve ters okumaları analiz etmek için gereklidir.",
   "Stringleri tersine çevirmek için 2016b sonrasında `reverse()` fonksiyonu gelmiştir. Eski sürümlerde matris indekslemesi `dizi(end:-1:1)` kullanılır.",
   "<li>Modern MATLAB için `reverse(dna)` kullanın.</li><li>Veya alternatif olarak indeksleme mantığını `dna(end:-1:1)` şeklinde kurarak diziyi sondan başa tarayın.</li>"),

  ("Ters Tamamlayıcı (Reverse Complement)", "AAAACCCGGT", "ACCGGGTTTT",
   "Bir DNA dizisinin ters tamamlayıcısını bulun (A->T, C->G, sonra tersine çevir).",
   "dna='AAAACCCGGT';\nt = dna; t(dna=='A')='T'; t(dna=='T')='A'; t(dna=='C')='G'; t(dna=='G')='C';\ndisp(t(end:-1:1));",
   "Çift iplikli DNA'da bir iplik 5' den 3' yönüne uzanırken, karşı iplik tamamlayıcı (komplementer) bazlarla 3' den 5' yönüne uzanır. Veri tabanlarında genellikle sadece tek iplik kaydedilir, diğerini bulmak için ters tamamlayıcı hesaplanır.",
   "Karakter yer değiştirmeyi eşzamanlı yapmak için sıralı `strrep` kullanmak risklidir (A'yı T yapıp, sonra T'yi tekrar A yapma hatası). Güvenli yol mantıksal indeksleme ile haritalamadır.",
   "<li>Dizinin bir kopyasını oluşturun.</li><li>Mantıksal indeksleme ile (`dna == 'A'`) kopya üzerinde yerlerine 'T' yazın. Bunu tüm bazlar için yapın.</li><li>Elde edilen tamamlayıcı diziyi sondan başa doğru (tersine) çevirin.</li>"),

  ("RNA'dan DNA'ya Ters Transkripsiyon", "AUGGCUACUUAA", "ATGGCTACTTAA",
   "RNA dizisini tekrar DNA'ya çeviren bir kod yazın (U yerine T).",
   "rna = 'AUGGCUACUUAA';\ndna = strrep(rna, 'U', 'T');\ndisp(dna);",
   "Retrovirüsler (örneğin HIV), kendi RNA genomlarını kullanarak ev sahibi hücrede DNA sentezlemek için Ters Transkriptaz enzimini kullanırlar. Bu, Merkezî Doğma'nın tersine işleyen bir kuraldır.",
   "RNA'yı DNA'ya çevirmenin programlamadaki karşılığı, Transkripsiyon işleminin tam tersi olan `strrep` kullanımıdır.",
   "<li>`strrep` fonksiyonunu kullanarak dizideki tüm 'U' harflerini bulup 'T' ile değiştirin.</li>"),

  ("Motif Arama", "GATATATGCATATACTT", "8",
   "Büyük bir DNA dizisi içinde belirli bir motifin kaçıncı indekste başladığını bulun.",
   "dna = 'GATATATGCATATACTT';\nindeks = strfind(dna, 'ATGC');\ndisp(indeks);",
   "Gen regülasyonunda, transkripsiyon faktörleri DNA üzerindeki özel kısa dizilere (motiflere) bağlanır. Bu motifleri bulmak gen analizinin temelidir.",
   "MATLAB'da bir metin içinde başka bir metin aramak için `strfind` kullanılır. Bu fonksiyon motifin başladığı indekslerin bir dizisini döndürür.",
   "<li>`strfind(buyuk_dizi, aranacak_motif)` şeklinde fonksiyonu çağırın.</li><li>Dönen indeksi (veya indeks listesini) ekrana yazdırın.</li>"),

  ("Sadece Pürinleri Filtreleme", "ATCGATCG", "A G A G",
   "Dizideki sadece pürinleri (A, G) koruyup diğerlerini boşluk yapın.",
   "dna = 'ATCGATCG';\np = dna;\np(dna == 'T' | dna == 'C') = ' ';\ndisp(p);",
   "Nükleotidler halka yapılarına göre pürin (iki halkalı: Adenin, Guanin) ve pirimidin (tek halkalı: Sitozin, Timin) olarak ikiye ayrılır. Mutasyonlar genellikle aynı gruptaki bazlar arasında gerçekleşir (Transisyon).",
   "Birden fazla koşulu kontrol etmek için Mantıksal VEYA (`|`) operatörü kullanılır.",
   "<li>Dizinin bir kopyasını çıkarın.</li><li>`dna == 'T' | dna == 'C'` ile pirimidin olan yerleri bulun.</li><li>Kopya dizide bu yerlere boşluk karakteri (' ') atayın.</li>"),

  ("Sadece Pirimidinleri Filtreleme", "ATCGATCG", " TC  TC ",
   "Dizideki sadece pirimidinleri (C, T) koruyup diğerlerini boşluk yapın.",
   "dna = 'ATCGATCG';\np = dna;\np(dna == 'A' | dna == 'G') = ' ';\ndisp(p);",
   "DNA yapısında bir pürin daima bir pirimidin ile eşleşerek sarmalın sabit genişlikte kalmasını sağlar. Ultraviyole ışık, yan yana gelen pirimidinler arasında zararlı bağlar (pirimidin dimerleri) oluşturabilir.",
   "Yine mantıksal indeksleme ve Mantıksal VEYA (`|`) operatörü ile filtreleme yapılır.",
   "<li>`dna == 'A' | dna == 'G'` ile pürinleri bulun ve kopyalanmış dizide buralara boşluk karakteri atayın.</li>"),

  ("Mutasyon (Hamming Mesafesi) Hesabı", "GAGCCT..., CATCGT...", "7",
   "İki diziyi karşılaştırarak farklı nükleotidlere sahip konumların sayısını bulun.",
   "d1='GAGCCTACTAACGGGAT'; d2='CATCGTAATGACGGCCT';\nfark = sum(d1 ~= d2);\ndisp(fark);",
   "İki homolog dizi (aynı atadan gelen diziler) arasındaki farklı nükleotid sayısı, evrimsel mesafeyi ve mutasyon oranını ölçmekte kullanılan temel bir metriktir. Bilgisayar biliminde buna Hamming Mesafesi denir.",
   "İki dizi eşit uzunluktaysa, `~=` (eşit değil) operatörü iki diziyi eleman eleman karşılaştırır ve fark olan yerlerde 1 döndürür.",
   "<li>`d1 ~= d2` ifadesi ile iki diziyi karşılaştırın.</li><li>Çıkan mantıksal sonucu `sum()` ile toplayarak toplam mutasyon sayısını elde edin.</li>"),

  ("Dizi Ligasayonu", "ATGC, GTAC", "ATGCGTAC",
   "İki farklı DNA parçasını birbirine bağlayan bir kod yazın.",
   "p1='ATGC'; p2='GTAC';\nbirlesik=[p1, p2];\ndisp(birlesik);",
   "Ligaz enzimleri, laboratuvarda iki farklı DNA parçasını birbirine bağlamak (rekombinant DNA teknolojisi) için kullanılır. Bu işlem yazılımda string birleştirme olarak modellenir.",
   "MATLAB'da iki string dizisini birleştirmek için en kolay yol, yatay vektör birleştirme köşeli parantezi `[string1, string2]` kullanmaktır.",
   "<li>İki diziyi köşeli parantez içinde virgül veya boşlukla ayırarak yan yana koyun.</li>"),

  ("Nükleotid Standartlaştırma", "atgCgtA", "ATGCGTA",
   "Tüm nükleotidleri büyük harfe çeviren bir kod yazın.",
   "dna = 'atgCgtA';\ndisp(upper(dna));",
   "Biyoinformatik veritabanlarından çekilen sekanslar farklı formatlarda (küçük/büyük harf karışık) olabilir. Analiz öncesinde veri temizliği ve standardizasyon hayati önem taşır.",
   "String içindeki tüm karakterleri büyük harfe dönüştürmek için `upper()` fonksiyonu kullanılır.",
   "<li>Standartlaştırma için diziyi `upper()` fonksiyonunun içine koyun ve sonucu yazdırın.</li>"),

  ("Bilinmeyen Nükleotidleri Sayma", "ATGNNNCGATN", "4",
   "Dizideki toplam okunamayan 'N' sayısını bulan bir kod yazın.",
   "dna = 'ATGNNNCGATN';\ndisp(sum(dna == 'N'));",
   "Modern sekanslama cihazları (Next-Gen Sequencing) bir bazı okurken sinyal yeterince net değilse hata yapmamak adına o noktaya 'N' (Any Nucleotide) yazar. Yüksek 'N' sayısı düşük veri kalitesini gösterir.",
   "Belirli bir harfi saymak için mantıksal maske ve toplama kombosu idealdir.",
   "<li>`dna == 'N'` ile bilinmeyen noktaları tespit edin ve `sum()` ile toplamını alın.</li>"),

  ("Başlangıç Kodonunu Kontrol Etme", "ATGCGTACG", "1",
   "Dizinin protein sentezine başlatıcı kodon olan 'ATG' ile başlayıp başlamadığını kontrol edin.",
   "dna = 'ATGCGTACG';\ndisp(startsWith(dna, 'ATG'));",
   "Hücrede protein sentezi (translasyon) her zaman Metiyonin amino asidini kodlayan 'ATG' (RNA'da AUG) başlangıç kodonu ile başlar. Gen bulma algoritmaları her zaman bu işareti arar.",
   "Bir stringin belirli bir alt string ile başlayıp başlamadığını kontrol etmek için modern MATLAB'da `startsWith` mantıksal fonksiyonu bulunur.",
   "<li>`startsWith(dizi, 'ATG')` çağrısını kullanarak mantıksal 1 (Doğru) veya 0 (Yanlış) sonucunu alın.</li>"),

  ("Bitiş Kodonunu Kontrol Etme", "ATGCGTTAA", "1",
   "Dizinin bitiş kodonlarından biriyle (TAA, TAG veya TGA) bitip bitmediğini kontrol edin.",
   "dna = 'ATGCGTTAA';\ndisp(endsWith(dna, 'TAA') | endsWith(dna, 'TAG') | endsWith(dna, 'TGA'));",
   "Ribozom, mRNA'yı okurken TAA, TAG veya TGA (UAA, UAG, UGA) dizilerinden birine geldiğinde protein sentezini sonlandırır. Buna 'Stop Codon' denir.",
   "Bir metnin belirli bir sonla bitip bitmediği `endsWith` ile kontrol edilir. Birden fazla koşul için VEYA (`|`) operatörü zincirlenir.",
   "<li>Her üç bitiş kodonu için ayrı ayrı `endsWith()` çağrısı yapın.</li><li>Sonuçları `|` operatörü ile birleştirerek herhangi birinin varlığını kontrol edin.</li>"),

  ("Nükleotid Konumu", "ATGCG", "G",
   "Bir DNA dizisinin tam ortasındaki (merkezindeki) nükleotidi bulun.",
   "dna = 'ATGCG';\norta = ceil(length(dna) / 2);\ndisp(dna(orta));",
   "Pencereleme (sliding window) gibi ileri düzey algoritmalarda dizinin merkez eksenini ve konumunu belirlemek, pivot işlemlerini hızlandırır.",
   "MATLAB indeksleri 1'den başlar. Uzunluğun yarısını alıp yukarı yuvarlamak (`ceil`) için orta noktayı bulmak en güvenli yöntemdir.",
   "<li>Uzunluğu 2'ye bölüp `ceil()` ile üst tam sayıya yuvarlayarak indeksi bulun.</li><li>Diziye bu indeks numarası ile erişin: `dizi(indeks)`.</li>"),

  ("Alt Dizi (Subsequence) Çıkarma", "ATGCGTACGTCG", "GCGTA",
   "Bir DNA dizisinin 3. nükleotidinden başlayıp 7. nükleotidi dahil olmak üzere aradaki parçayı çıkarın.",
   "dna = 'ATGCGTACGTCG';\ndisp(dna(3:7));",
   "Tüm bir genomu değil de sadece belirli bir gen bölgesini kesip almak (slicing), genomik veritabanlarında arama yaparken (örneğin BLAST algoritması) en çok yapılan veri ayırma işlemidir.",
   "MATLAB'da iki nokta üst üste operatörü (`başlangıç:bitiş`), bir vektörden veya karakter dizisinden alt bölüm (slice) almak için kullanılır.",
   "<li>`dna(3:7)` şeklinde başlangıç ve bitiş indekslerini belirterek alt diziyi çıkarın.</li>"),

  ("Polindromik DNA Dizisi", "GCGC", "1",
   "Dizinin palindromik (kendi tersi ile aynı) olup olmadığını kontrol edin.",
   "dna = 'GCGC';\nters = dna(end:-1:1);\ndisp(strcmp(dna, ters));",
   "Biyolojide palindromik diziler, restriksiyon enzimleri (DNA'yı kesen moleküler makaslar) tarafından tanınan özel bölgelerdir (örneğin EcoRI enzimi GAATTC dizisini keser).",
   "İki karakter dizisinin tamamen eşit olup olmadığını kontrol etmek için `strcmp` (string compare) kullanılır, `==` kullanmak boyutlar uyuşmazsa hata verir.",
   "<li>Diziyi `(end:-1:1)` ile ters çevirin.</li><li>`strcmp(dizi, tersi)` ile orijinaliyle tersini karşılaştırıp mantıksal sonucu elde edin.</li>"),

  ("Motif Frekansı", "CGCGCGCG", "4",
   "Belirli bir ikili nükleotidin (dinükleotid, örneğin 'CG') toplam kaç kez geçtiğini sayın.",
   "dna = 'CGCGCGCG';\nindeksler = strfind(dna, 'CG');\ndisp(length(indeksler));",
   "İnsan genomunda CG dinükleotidleri (CpG bölgeleri) metilasyon denilen epigenetik bir işlemle susturulabilir. Bu bölgelerin yoğunluğunu hesaplamak epigenetik analizler için önemlidir.",
   "`strfind` fonksiyonu motifin geçtiği tüm başlangıç noktalarını döndürür. Bu sonucun uzunluğu (`length`), motifin geçiş sayısını verir.",
   "<li>`strfind` ile motifleri bulun.</li><li>Dönen indeks vektörünün eleman sayısını `length` ile hesaplayarak frekansı bulun.</li>")
]

problems_list = []

for i, (title, inp, out, desc, code, bio, mat, steps) in enumerate(p_data):
    explanation = base_exp.format(bio=bio, matlab=mat, steps=steps)
    problems_list.append({
        "id": f"b{i+1}",
        "level": "beginner",
        "title": f"{i+1}. {title}",
        "description": f"<p>{desc}</p><br/><p><b>Girdi:</b> <code>{inp}</code></p><p><b>Beklenen Çıktı:</b> <code>{out}</code></p>",
        "starter_code": "% Kodunuzu buraya yazın\n\n",
        "solution_code": code,
        "expected_output": out,
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

