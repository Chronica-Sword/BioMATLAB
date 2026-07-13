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
        "id": "i11", "level": "intermediate",
        "title": "11. Biyolojik Matris Geri İzleme (Traceback) Yönleri",
        "description": "<p>Hizalama matrisindeki bir hücrenin (i, j) değerinin, üstünden mi (Gap), solundan mı (Gap) yoksa çaprazından mı (Match/Mismatch) geldiğini bulan bir karar mekanizması yazın.</p><br/><p><b>Girdi:</b> <code>M(i,j)=5, sol=3, ust=3, capraz=4, gap=-2, match=1</code></p><p><b>Beklenen Çıktı:</b> <code>'Çaprazdan Geldi'</code> (Çünkü 4+1 = 5)</p>",
        "starter_code": "matris_hucre = 5;\nsol_deger = 3;\nust_deger = 3;\ncapraz_deger = 4;\ngap_cezasi = -2;\nmatch_odulu = 1;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "matris_hucre = 5;\nsol_deger = 3;\nust_deger = 3;\ncapraz_deger = 4;\ngap_cezasi = -2;\nmatch_odulu = 1;\n\n% Hangi yoldan geldiğini buluyoruz\nif capraz_deger + match_odulu == matris_hucre\n    disp('Çaprazdan Geldi (Eşleşme)');\nelseif sol_deger + gap_cezasi == matris_hucre\n    disp('Soldan Geldi (1. Dizide Boşluk)');\nelseif ust_deger + gap_cezasi == matris_hucre\n    disp('Üstten Geldi (2. Dizide Boşluk)');\nelse\n    disp('Hata: Matris hesabı uyuşmuyor');\nend",
        "expected_output": "Çaprazdan Geldi (Eşleşme)",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Geri İzleme ve Hizalama Çıktısı)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Needleman-Wunsch algoritmasında, <code>M+1 x N+1</code> boyutlarındaki skor matrisini baştan sona doldurmak işin sadece yarısıdır. Matrisin en sağ alt köşesinde elde ettiğiniz rakam (Örn: 24), iki dizinin maksimum benzerlik skorudur. Ancak biyologların asıl görmek istediği şey sadece skor değil, dizilerin yan yana nasıl dizildiğidir (A'nın karşısına C mi geldi, araya boşluk mu eklendi vb.).</p>
        <p>Hizalama (Alignment) dizilimini elde etmek için, matrisin en sağ alt köşesinden başlanır ve sol üst köşeye (0,0 noktasına) kadar <strong>Geri İzleme (Traceback)</strong> yapılır. Bulunduğunuz hücredeki değere nasıl ulaşıldığını anlamak için komşu hücrelere bakılır. Eğer değer sol üst çaprazdaki hücreden gelmişse bu, her iki diziden de birer harf alındığı (Match veya Mismatch) anlamına gelir. Eğer soldan gelmişse bir diziye, üstten gelmişse diğer diziye boşluk (Gap) eklendiği anlaşılır. Bu işlem geriye doğru gidilerek gerçek hizalama şablonunu çizer.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize herhangi bir anlık (i,j) noktasındaki ana matris değeri ve bu hücrenin üç komşusunun (sol, üst ve çapraz) değerleri veriliyor. Ayrıca ödül/ceza puanlarımız da belli. Amacımız, basit toplama işlemleri yaparak bu 5 değerine ulaşmak için hangi komşudan gelinmiş olması gerektiğini mantıksal bir sıra ile bulmak ve sonucu ekrana yazdırmaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Burası bir karar ağacı (if-elseif-else) yapısı gerektirir. Algoritmik tasarımda sıralama önemlidir. Çaprazdan gelme ihtimali (karakter eşleşmesi) biyolojik olarak ilk tercih edilmesi gereken yoldur, çünkü boşluklar (Gap) hizalamayı bozan sevilmeyen olaylardır. Bu nedenle ilk <code>if</code> kontrolünde her zaman çapraz değer sorgulanır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Eğer sol komşu ve üst komşu eşit skorlar üretiyorsa, birden fazla optimal yol var demektir. Genelde yazılımlar önceden belirlenmiş bir hiyerarşiye (örn: \"önce sola git\") uyarak tek bir yolu seçerler. İleri seviye algoritmalarda tüm yollar hafızada tutulup birden fazla alternatif hizalama sunulur.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>if capraz_deger + match_odulu == matris_hucre</code> : Önce çapraz komşuya bakıyoruz. Çaprazdan gelmenin kuralı, eşleşme veya eşleşmeme puanı eklenmesidir (Bu örnekte eşleşme kabul ediliyor). 4 + 1 işlemi 5'e eşit olduğu için şart sağlanır.</li>
        <li><code>disp('Çaprazdan Geldi');</code> : Mantıksal blok doğru çıkarsa hedef yol bulunduğundan çıktı yazdırılır ve alt satırlardaki sorgulara bakılmadan karar ağacı sonlanır.</li>
        <li><code>elseif sol_deger + gap_cezasi == matris_hucre</code> : Eğer çapraz tutmasaydı, sol hücre değerine boşluk cezası (3 + -2 = 1) eklenip 5'e eşit olup olmadığına bakılacaktı.</li>
        <li>Aynı kontrol üst hücre için de yapılarak Traceback yönü tespit edilir.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i12", "level": "intermediate",
        "title": "12. Spesifik GC İçeriğiyle Rastgele DNA Üretimi",
        "description": "<p>Tam olarak %70 GC içeriğine sahip 100 nükleotid uzunluğunda rastgele (sentetik) bir DNA dizisi üreten bir kod yazın.</p><br/><p><b>Girdi:</b> <code>uzunluk = 100, gc_hedefi = 0.70</code></p><p><b>Beklenen Çıktı:</b> 100 harflik dizi (İçinde rastgele dağılmış toplam 70 adet G/C ve 30 adet A/T bulunmalıdır)</p>",
        "starter_code": "uzunluk = 100;\ngc_hedefi = 0.70;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "uzunluk = 100;\ngc_hedefi = 0.70;\n% Önce hangi harften kaç tane olacağını bulalım\ngc_sayisi = round(uzunluk * gc_hedefi);\nat_sayisi = uzunluk - gc_sayisi;\n\nsentetik_dna = blanks(uzunluk);\n\n% GC harflerini atayalım (G ve C arasından rastgele)\nfor i = 1:gc_sayisi\n    if rand() > 0.5\n        sentetik_dna(i) = 'G';\n    else\n        sentetik_dna(i) = 'C';\n    end\nend\n\n% AT harflerini atayalım (A ve T arasından rastgele)\nfor i = gc_sayisi+1:uzunluk\n    if rand() > 0.5\n        sentetik_dna(i) = 'A';\n    else\n        sentetik_dna(i) = 'T';\n    end\nend\n\n% Son olarak harflerin yerlerini karıştıralım (Shuffle)\n% randperm() fonksiyonu dizinin indekslerini rastgele sıralar\nkarisik_indeksler = randperm(uzunluk);\nsentetik_dna = sentetik_dna(karisik_indeksler);\n\ndisp(sentetik_dna);",
        "expected_output": "(Rastgele. Örn: GCGCATCGGCGGCC... (%70 GC içerir))",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Sentetik Biyoloji ve Mock Veri)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatik algoritmalarını test etmek için her zaman gerçek biyolojik verilere sahip olamayız. Bazen belirli istatistiksel özelliklere (örneğin aşırı yüksek GC içeriğine sahip uç durumlar) sahip \"Mock\" (sahte/sentetik) verilere ihtiyaç duyarız. Ayrıca Sentetik Biyoloji alanında, sıfırdan gen tasarlanırken veya belirli bir termal kararlılığa (Tm sıcaklığına) sahip yapay primerler üretilirken bu tür algoritmik jeneratörler kullanılır.</p>
        <p>Doğal bir diziyi rastgele mutasyona uğratmaktan farklı olarak (Markov Zincirleri), bu işlem sıfırdan (De Novo) bir veri yaratımıdır. Rastgelelik içerir ancak sınırı önceden çok net çizilmiştir: Ortaya çıkan dizinin %70'i G veya C olmak zorundadır. Bu, biyoinformatik test (benchmark) süreçlerinin standart veri üretim (mock data generation) pratiğidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize toplam uzunluk (100) ve GC oranı (0.70) veriliyor. Doğrudan 100 kere zar atıp %70 ihtimalle G/C üretmek (Binom Dağılımı) istatistiksel olarak bizi hedefe yaklaştırır ancak tam olarak %70 çıkmasını garanti etmez (68 de çıkabilir, 73 de çıkabilir). Tam olarak 70 adet G/C olmasını sağlamak için farklı bir algoritma kurulmalıdır. Havuza tam olarak 70 tane G/C ve 30 tane A/T konulmalı, sonra bu havuz rastgele karıştırılmalıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Algoritmamız üç aşamadan oluşur: Ön Tahsis (Pre-allocation), Havuzu Doldurma ve Karıştırma (Shuffle). Önce dizinin başına peş peşe 70 adet G veya C yazarız, sonra kalan 30 yere A veya T yazarız (GGGCC...C|AAT...T). Daha sonra MATLAB'ın eşsiz karıştırma fonksiyonu olan <code>randperm()</code> (Random Permutation) fonksiyonunu kullanarak dizinin indekslerini bir tombala torbasındaymış gibi iyice karıştırır (Shuffle) ve yeni indekslere göre diziyi yeniden sıralarız.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da bir vektörün elemanlarını karıştırmanın en kısa ve zarif yolu <code>dizi(randperm(length(dizi)))</code> sintaksıdır. Birçok farklı programlama dilinde bu işlemi yapmak için uzun Fisher-Yates shuffle döngüleri yazmanız gerekir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>gc_sayisi = round(uzunluk * gc_hedefi);</code> : Toplam uzunluk üzerinden matematiksel hesabımızı yapıyoruz. (100 * 0.70 = 70)</li>
        <li><code>sentetik_dna = blanks(uzunluk);</code> : Önceden 100 harflik bir boş uzay yaratıyoruz.</li>
        <li>İlk <code>for</code> döngüsünde 1'den 70'e kadar ilerliyor ve 0.5 ihtimal (yazı-tura) ile 'G' veya 'C' ataması yapıyoruz.</li>
        <li>İkinci <code>for</code> döngüsünde 71'den 100'e kadar ilerleyerek aynı mantıkla 'A' veya 'T' ataması yapıyoruz.</li>
        <li><code>karisik_indeksler = randperm(uzunluk);</code> : Bize 1 ile 100 arasında tamamen karmaşık sıralanmış (örn: [54, 2, 99, 17...]) bir sayısal vektör verir.</li>
        <li><code>sentetik_dna = sentetik_dna(karisik_indeksler);</code> : Elde edilen bu rastgele tombala sayıları, orijinal dizinin indeks numaraları yerine geçirilir ve harfler havada yer değiştirerek tamamen rastgele bir sıralamaya kavuşur.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i13", "level": "intermediate",
        "title": "13. Kodon Kullanım Sıklığı (Codon Bias)",
        "description": "<p>Aynı amino asidi şifreleyen (sinonim) kodonların kullanım oranlarını hesaplayın. Verilen RNA dizisinde Fenilalanin (F) amino asidini kodlayan UUU ve UUC kodonlarının bulunma oranını kıyaslayın.</p><br/><p><b>Girdi:</b> <code>rna='UUU...UUC...UUU'</code> (60 harflik sekans)</p><p><b>Beklenen Çıktı:</b> <code>UUU: 2 adet, UUC: 1 adet</code></p>",
        "starter_code": "rna = 'AUGUUUGGCUUCUAAAACUUUCAGUUC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "rna = 'AUGUUUGGCUUCUAAAACUUUCAGUUC';\nuuu_sayisi = 0;\nuuc_sayisi = 0;\n\n% RNA'yı üçerli okumamız gerekir\nfor i = 1:3:length(rna)-2\n    kodon = rna(i:i+2);\n    if strcmp(kodon, 'UUU')\n        uuu_sayisi = uuu_sayisi + 1;\n    elseif strcmp(kodon, 'UUC')\n        uuc_sayisi = uuc_sayisi + 1;\n    end\nend\n\nfprintf('UUU Sayısı: %d\\n', uuu_sayisi);\nfprintf('UUC Sayısı: %d\\n', uuc_sayisi);",
        "expected_output": "UUU Sayısı: 2\nUUC Sayısı: 2",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Codon Bias - Kodon Yanlılığı)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Genetik kod dejeneredir; yani bir amino asit birden fazla kodon tarafından şifrelenebilir (Örneğin Fenilalanin için UUU ve UUC). Ancak hücreler bu eşanlamlı (sinonim) kodonları eşit oranda (%50 - %50) kullanmazlar. Bazı canlı türleri UUU'yu çok daha sık kullanırken (Codon Bias), başka bir bakteri türü UUC'yi tercih edebilir. Bu tercih, o hücrenin sitoplazmasında bulunan tRNA moleküllerinin bolluğu ile doğrudan ilişkilidir.</p>
        <p>Biyoinformatikte Codon Bias (Kodon Kullanım Eğilimi) analizi çok önemlidir. Eğer insan kaynaklı bir geni (örneğin İnsülin geni) alıp bir bakterinin (E. coli) içine koyup üretmesini isterseniz, bakteri kendi \"şivesine\" (codon bias) uymayan bu yeni geni verimli şekilde okuyamayabilir ve protein üretimi çok düşük kalabilir. Bu yüzden laboratuvar öncesi Gen Optimizasyonu (Kodon Optimizasyonu) süreçlerinde, genin amino asit sırası değiştirilmeden, içindeki kodonlar hedef bakterinin sevdiği kodonlarla (örn: tüm UUU'lar UUC ile) değiştirilir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Verilen uzun bir RNA dizisini 3'lü okuma çerçevelerine (Reading Frames) uygun şekilde baştan sona taramamız gerekmektedir. Kaydırıcı pencerenin (sliding window) her adımda 1 değil, tam olarak 3 adım atlaması gerekir (Kodonların bölünmemesi için). Çıkarılan her bir 3'lü parçanın UUU veya UUC olup olmadığı kontrol edilecek ve ilgili sayaçlar artırılacaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Sıradan bir <code>strfind()</code> kullanımı burada biyolojik bir hataya neden olur. <code>strfind(rna, 'UUU')</code> komutu, dizinin okuma çerçevesine (1. indeks, 4. indeks, 7. indeks vb.) bakmaz, herhangi bir yerden bulduğu UUU'ları getirir (örneğin 2. indeksten başlayan bir UUU). Bu yanlıştır. Protein translasyonu frame-shift (çerçeve kayması) olmadan katı bir şekilde 3'er 3'er ilerler. Bu yüzden adım aralığı (step size) 3 olan bir <code>for</code> döngüsü kurmak zorunludur.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Döngülerde başlangıç:adım:bitiş mantığı <code>1:3:length</code> şeklindedir. Eğer bir geni 2. indeksten okumaya başlasaydık (Alternative Reading Frame), o zaman <code>2:3:length</code> yazardık.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>uuu_sayisi = 0; uuc_sayisi = 0;</code> : Her iki kodon için de başlangıç frekans sayaçları oluşturulur.</li>
        <li><code>for i = 1:3:length(rna)-2</code> : Döngümüz 1. nükleotidden başlar, birer birer değil üçer üçer (3) atlayarak ilerler. Sınır taşımasını önlemek için bitişten 2 çıkarılır.</li>
        <li><code>kodon = rna(i:i+2);</code> : i, i+1 ve i+2 olmak üzere tam 3 karakterlik bir slice alınır. (Örn: i=4 ise 4, 5 ve 6. harfler).</li>
        <li><code>if strcmp(kodon, 'UUU')</code> : Eğer okunan parça karakter olarak birebir 'UUU'ya eşitse sayaç 1 artırılır. Aynı işlem 'UUC' için de <code>elseif</code> bloğunda yapılır.</li>
        <li><code>fprintf</code> ile iki kodonun da bu dizideki genetik kullanımı ekrana dökülür.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i14", "level": "intermediate",
        "title": "14. Çift İplikli (Double Stranded) DNA Modeli Bastırma",
        "description": "<p>Bir DNA dizisini (5' -> 3' yönünde) alın, altına bağlantı bağlarını temsil eden dikey çubuklar ('|') koyun ve en alta da ters tamamlayıcı ipliği (3' -> 5' yönünde) yazdırarak çift sarmallı bir DNA modelini ekrana üç satır halinde çizin.</p><br/><p><b>Girdi:</b> <code>dna='ATGC'</code></p><p><b>Beklenen Çıktı:</b><br/>5'-ATGC-3'<br/>   ||||   <br/>3'-TACG-5'</p>",
        "starter_code": "dna = 'ATGC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'ATGC';\n\n% Tamamlayıcı ipliği buluyoruz (Sırasını bozmadan)\nkomplementer = dna;\nkomplementer(dna=='A') = 'T';\nkomplementer(dna=='T') = 'A';\nkomplementer(dna=='C') = 'G';\nkomplementer(dna=='G') = 'C';\n\n% Aradaki hidrojen bağlarını temsil eden çubuklar\nbaglar = repmat('|', 1, length(dna));\n\n% Ekrana görsel olarak hizalı biçimde basıyoruz\nfprintf('5\\''-%s-3\\''\\n', dna);\nfprintf('   %s   \\n', baglar);\nfprintf('3\\''-%s-5\\''\\n', komplementer);",
        "expected_output": "5'-ATGC-3'\n   ||||   \n3'-TACG-5'",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Antiparalel Çift Sarmal)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>DNA modeli Watson ve Crick tarafından ortaya konulduğunda en dikkat çekici özelliği, bir merdiven yapısında olması ve iki ipliğin birbirine ters yönlerde (Antiparalel) akmasıydı. Bir ipliğin Karbon 5' ucu, karşı ipliğin Karbon 3' ucuna denk gelir. Aradaki merdiven basamakları ise zayıf hidrojen bağlarıdır.</p>
        <p>Bilgisayar ekranında (ASCII ortamında) genomik verileri görselleştirmek, dizilim (alignment) sonuçlarını insan gözünün anlayabileceği formata sokmak için olmazsa olmazdır. Tüm biyoinformatik arayüzleri, mutasyonları ve eşleşmeleri bu \"üç satırlık\" (sense ipliği, aradaki bağlar, antisense ipliği) modelleme üzerinden araştırmacılara gösterir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Tek satırlık bir metin dizisinden yola çıkarak konsolda 3 satırlık bir görsel tasarım elde etmeliyiz. Birinci satıra orijinal diziyi (başına ve sonuna 5' ve 3' ekleyerek), ikinci satıra dizi uzunluğu kadar dikey çubuk ('|'), üçüncü satıra ise eşlenik diziyi (ancak ters çevirmeden, doğrudan karşılığıyla) başına 3' ve sonuna 5' ekleyerek basmalıyız. Başlıkların (5'-) karakter uzunluklarının alt ve üst satırlarda tam hizalanması kritiktir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Araya dizeceğimiz dikey çubukları döngüyle tek tek yazdırmak yerine MATLAB'ın Matris Kopyalama (Replication) fonksiyonu olan <code>repmat()</code> kullanılır. Bu, verilen bir karakteri veya matrisi istenilen boyutlarda çoğaltır. Dizinin eşleniğini bulurken, bu kez <code>reverse</code> kullanmıyoruz çünkü harfleri fiziksel olarak alt alta, karşılıklı hizalamak istiyoruz.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> <code>fprintf</code> içinde tek tırnak (<code>'</code>) yazdırmak istediğinizde, MATLAB bunu string kapatma karakteri sanıp hata verecektir. Bunu atlatmak için iki adet yan yana tek tırnak (<code>''</code>) kullanmalısınız (Kaçış sekansı - Escaping). (Örn: <code>'5''-ATGC'</code>).
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>komplementer = dna;</code> ve devamındaki 4 satırda dizinin sadece eşleniklerini (A-T, C-G) üretiyoruz. Reverse (tersine çevirme) işlemi yapmıyoruz, çünkü grafiksel gösterimde sağ baştaki harf, sağ baştaki harfin tam altına oturmalıdır.</li>
        <li><code>baglar = repmat('|', 1, length(dna));</code> : Bir satır ve DNA uzunluğu kadar sütun boyutunda, içi sadece dikey çubuklarla dolu bir vektör kopyası oluşturuyoruz. </li>
        <li><code>fprintf('5\\''-%s-3\\''\\n', dna);</code> : Birinci satırı basıyoruz. Baştaki <code>5'-</code> eki toplam 3 karakter yer kapladığı için, alt satırı basarken hizalama amacıyla başa 3 adet boşluk koyacağız.</li>
        <li><code>fprintf('   %s   \\n', baglar);</code> : Orta satır. Başında ve sonunda 3'er boşluk var ki bağlar tam olarak gen harflerinin altına hizalansın.</li>
        <li><code>fprintf('3\\''-%s-5\\''\\n', komplementer);</code> : Üçüncü satırı, komplementer diziyi kullanarak basıyoruz. Uçlar ters yönlü (3' ve 5') olarak etiketlenmiştir.</li>
    </ul>
</div>
        """
    },
    {
        "id": "i15", "level": "intermediate",
        "title": "15. Çoklu Hizalamadan Konsensüs (Ortak) Dizi Bulma",
        "description": "<p>Eşit uzunlukta üç farklı DNA dizisi veriliyor. Bu dizileri alt alta düşünerek, her bir sütunda en çok tekrar eden (çoğunluk oyu alan) nükleotidi bularak yeni bir \"Konsensüs\" (Ortak/Uzlaşı) dizisi oluşturan bir kod yazın.</p><br/><p><b>Girdi:</b> <code>d1='ATGC', d2='AAGC', d3='ATTC'</code></p><p><b>Beklenen Çıktı:</b> <code>ATGC</code> (Sütunlar: AAA->A, TAG->T, GGT->G, CCC->C)</p>",
        "starter_code": "d1 = 'ATGC';\nd2 = 'AAGC';\nd3 = 'ATTC';\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "d1 = 'ATGC';\nd2 = 'AAGC';\nd3 = 'ATTC';\n\nkonsensus = blanks(length(d1));\n\nfor i = 1:length(d1)\n    % O sütundaki 3 harfi bir diziye koyuyoruz\n    sutun = [d1(i), d2(i), d3(i)];\n    \n    % Mod (mode) istatistiği: Dizide en çok tekrar eden elemanı bulur\n    % Karakter dizilerinde doğrudan çalışmayabileceği için her karakteri sayıyoruz:\n    \n    a_say = sum(sutun == 'A');\n    t_say = sum(sutun == 'T');\n    c_say = sum(sutun == 'C');\n    g_say = sum(sutun == 'G');\n    \n    % En büyük frekansa sahip nükleotidi bulma\n    sayilar = [a_say, t_say, c_say, g_say];\n    harfler = ['A', 'T', 'C', 'G'];\n    \n    [~, maks_indeks] = max(sayilar);\n    konsensus(i) = harfler(maks_indeks);\nend\n\ndisp(konsensus);",
        "expected_output": "ATGC",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Multiple Sequence Alignment - MSA)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Aynı gen ailesinin farklı türlerdeki (örneğin İnsan, Fare ve Şempanze insülin geni) dizilimleri evrim boyunca mutasyonlar geçirse de, genin fonksiyonunu yerine getirmesini sağlayan kritik (korunmuş - conserved) bölgeler değişmeden kalır. Biyoinformatikte birden fazla dizi alt alta hizalandığında (Multiple Sequence Alignment), her bir hizalama sütununa dikey olarak bakılır ve evrimsel olarak en çok tercih edilen harf seçilir. Bu şekilde oluşturulan ideal ve genelleştirilmiş hayali diziye <strong>Konsensüs (Uzlaşı) Dizisi</strong> denir.</p>
        <p>Konsensüs dizileri, promotör dizilimlerini (örn. Pribnow kutusu: TATAAT) tanımlamak, virüslerin (örn. Grip virüsünün) mutasyon geçirmeyen zayıf noktalarını bularak evrensel aşılar tasarlamak için kullanılan temel moleküler biyoloji araçlarından biridir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Girdi olarak aynı uzunlukta üç farklı dizi (vektör) alıyoruz. Amacımız yatay olarak değil, dikey olarak (sütun sütun) ilerlemek. Her adımda 1. dizinin i. karakteri, 2. dizinin i. karakteri ve 3. dizinin i. karakteri alınarak bir alt küme (sütun) oluşturulmalı. Daha sonra bu sütun içindeki harflerin frekansları sayılmalı ve en çok tekrar eden (matematiksel tabirle \"Mod\" değeri olan) harf, sonuç dizisinin (konsensüs) i. karakteri olarak kaydedilmelidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve Algoritma</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bu problemi çözmek için sayısal istatistikteki <code>mode()</code> fonksiyonunu karakterlere uyarlamak veya her harfin frekansını elle saymak mümkündür. Tüm dizileri birleştirip (3 x N) boyutunda iki boyutlu (2D) bir karakter matrisi oluşturmak (örn: <code>matris = [d1; d2; d3]</code>) işlemi daha da basitleştirebilir. Bu çözümümüzde okunabilirliği yüksek tutmak için for döngüsü ile dikey sütunları tek tek sayıyoruz. Dizideki maksimum sayıyı bulup onun indeksini almak için <code>max()</code> fonksiyonunun ikinci dönüş argümanını (maks_indeks) kullanacağız.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da <code>[deger, indeks] = max(vektor);</code> komutu, vektördeki en büyük sayıyı <code>deger</code> değişkenine atarken, o sayının vektörün kaçıncı sırasında olduğunu <code>indeks</code> değişkenine atar. Bu çok özellikli indeksleme yaklaşımı MATLAB veri analizinin kalbidir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>konsensus = blanks(length(d1));</code> : Nihai uzlaşı dizimizi tutacak boş (sıfırlanmış/pre-allocated) bir string vektörü oluşturuyoruz.</li>
        <li><code>sutun = [d1(i), d2(i), d3(i)];</code> : Döngünün her bir adımında, o indekste bulunan tüm dizilerdeki harfleri toplayıp yan yana (1x3) yatay bir vektör yapıyoruz. (Örn 2. indeks için: ['T', 'A', 'T']).</li>
        <li><code>a_say = sum(sutun == 'A');</code> vb... : Bu küçük sütun dizisinde hangi harften kaç adet olduğunu mantıksal toplama ile sayıyoruz.</li>
        <li><code>sayilar = [a_say, t_say, c_say, g_say];</code> : Elde edilen 4 frekansı yine bir vektöre koyuyoruz (Örn: [1, 2, 0, 0] -> 1 A, 2 T var).</li>
        <li><code>harfler = ['A', 'T', 'C', 'G'];</code> : Sayılarla paralel aynı sıraya (A,T,C,G) sahip bir referans harf vektörü tanımlıyoruz.</li>
        <li><code>[~, maks_indeks] = max(sayilar);</code> : Sayılar vektöründeki en büyük rakamın (Örn: 2'nin) hangi indekste (sırada) olduğunu buluyoruz. İlk değer olan (~) tilde işareti, sayının kendisine ihtiyacımız olmadığı için atlandığı anlamına gelir.</li>
        <li><code>konsensus(i) = harfler(maks_indeks);</code> : Bulduğumuz sıra numarasını referans harf listemize verip \"T\" harfini çekiyoruz ve konsensüs dizimizin i. elemanı yapıyoruz.</li>
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
