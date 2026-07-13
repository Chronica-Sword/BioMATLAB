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
        "id": "a4", "level": "advanced",
        "title": "4. Smith-Waterman Lokal Hizalama Algoritması (Negatif Sıfırlama)",
        "description": "<p>Smith-Waterman algoritmasını Needleman-Wunsch'tan ayıran tek ve en büyük kural şudur: Dinamik programlama matrisindeki bir hücrenin hesaplanan skoru 0'ın altına (negatife) düşemez. Hücre -2 olacaksa yerine 0 yazılır. Verilen sekanslar için Smith-Waterman matrisini doldurun ve matristeki maksimum (en yüksek) skoru bulun.</p><br/><p><b>Girdi:</b> <code>seq1='TGTTACGG', seq2='GGTTGACTA', match=3, mis=-3, gap=-2</code></p><p><b>Beklenen Çıktı:</b> Matristeki Maksimum Lokal Skor: <code>9</code> (GTT-AC vs GTTGAC bölgesi)</p>",
        "starter_code": "seq1 = 'TGTTACGG';\nseq2 = 'GGTTGACTA';\nmatch = 3; mis = -3; gap = -2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "seq1 = 'TGTTACGG';\nseq2 = 'GGTTGACTA';\nmatch = 3; mis = -3; gap = -2;\n\nm = length(seq1);\nn = length(seq2);\nskor_matrisi = zeros(m + 1, n + 1);\nmaksimum_skor = 0;\n\nfor i = 2:m+1\n    for j = 2:n+1\n        if seq1(i-1) == seq2(j-1)\n            s = match;\n        else\n            s = mis;\n        end\n        \n        yol_capraz = skor_matrisi(i-1, j-1) + s;\n        yol_ust    = skor_matrisi(i-1, j) + gap;\n        yol_sol    = skor_matrisi(i, j-1) + gap;\n        \n        % Smith-Waterman Kuralı: Dördüncü ihtimal olarak 0 eklenir\n        hucre_skoru = max([yol_capraz, yol_ust, yol_sol, 0]);\n        skor_matrisi(i, j) = hucre_skoru;\n        \n        % Global maksimumu takip et\n        if hucre_skoru > maksimum_skor\n            maksimum_skor = hucre_skoru;\n        end\n    end\nend\n\ndisp('Smith-Waterman Matrisi:');\ndisp(skor_matrisi);\nfprintf('Maksimum Lokal Hizalama Skoru: %d\\n', maksimum_skor);",
        "expected_output": "(Matris Bastırılır)\nMaksimum Lokal Hizalama Skoru: 9",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Lokal Hizalama vs Global Hizalama)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Evrimsel genomik analizlerin en büyük engellerinden biri, farklı canlıların genomlarının veya proteinlerinin tamamen aynı boyutta olmaması ve genellikle sadece küçük bir kısmının (örneğin aktif bir gen bölgesinin) işlevsel olarak korunmuş olmasıdır. Needleman-Wunsch algoritması (Global Hizalama), her iki diziyi de başından sonuna kadar uç uca eşleştirmeye zorlar. Eğer 100 harflik bir genin sadece ortasındaki 20 harf çok benziyor, geri kalan 80 harf tamamen alakasızsa, Needleman-Wunsch algoritması o 80 harfi zorla hizalamaya çalışırken o kadar çok eksi (ceza) puan alır ki, ortadaki o kıymetli 20 harflik benzerlik bölgesi negatif puanların içinde ezilip görünmez olur.</p>
        <p>1981 yılında Temple F. Smith ve Michael S. Waterman bu devasa biyolojik sorunu çözmek için çok basit ama dâhice bir matematiksel güncelleme önerdiler. Eğer bir hizalama kötüye gidiyorsa (skor sıfırın altına düşüyorsa), bu evrimsel olarak anlamsızdır ve \"Geçmişi Unutmalıyız\". Bir hücrenin değeri sıfırın altına düşerse onu zorla sıfır yaparız. Sıfır yapmak demek, yeni ve taze bir başlangıç yapmak, yani hizalamayı o noktadan sıfırdan yeniden başlatmak demektir. Bu küçük matematiksel hile (0 kuralı), algoritmanın devasa çöp yığınları içindeki en küçük \"Lokal\" (Yerel) adacıkları bile parlatarak bulmasını sağlar. Bugün NCBI BLAST dâhil dünyadaki tüm yerel hizalama arama motorları Smith-Waterman algoritmasının optimize edilmiş türevleridir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Amacımız, daha önceki Needleman-Wunsch algoritmasını Smith-Waterman mantığına çevirmektir. İlk önemli fark: Smith-Waterman'da ilk satır ve ilk sütun eksi boşluk cezalarıyla (-2, -4) DOLDURULMAZ, tamamen sıfır kalır (Çünkü ceza yedikçe sıfırlanma kuralı vardır). İkinci fark: Matrisin içindeki hücreleri hesaplarken yine 3 yolu (çapraz, üst, sol) deneriz, ancak bunlardan en büyüğünü seçerken listeye bir de 0 (Sıfır) sayısını dâhil ederiz. Eğer 3 yolun üçü de negatifse, sistem otomatik olarak 0'ı seçer. Üçüncü fark: Global hizalamada en yüksek skor daima matrisin sağ alt köşesindeydi. Ancak yerel hizalamada en yüksek skor matrisin <strong>herhangi bir yerinde</strong> olabilir. Bu yüzden döngü akarken karşılaştığımız gelmiş geçmiş en büyük sayıyı (Maksimum Lokal Skor) takip etmeli ve matris bittiğinde bu sayıyı yazdırmalıyız.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>MATLAB dilinde Smith-Waterman kuralını uygulamak sadece tek bir satır kod değiştirmekten ibarettir: <code>max([yol1, yol2, yol3])</code> ifadesine dördüncü bir eleman olarak 0 ekleriz: <code>max([yol1, yol2, yol3, 0])</code>. Bu kadar küçük bir sentaktik değişikliğin biyolojik çıktı üzerindeki etkisi muazzamdır. Maksimum skoru bulmak için matris bittikten sonra <code>max(skor_matrisi(:))</code> fonksiyonu kullanılabilir, ancak döngü içindeyken (on-the-fly) skoru kontrol edip bir değişkende tutmak (<code>if hucre_skoru > maksimum_skor</code>) genellikle hafıza yönetimi (Memory Management) açısından daha şık bir C/C++ alışkanlığıdır.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da <code>matris(:)</code> yazımı, iki boyutlu veya çok boyutlu bir matrisi tek boyutlu (1D) upuzun bir sütun vektörüne çevirir. Eğer matrisin tüm elemanları içindeki en büyük sayıyı bulmak isterseniz, <code>max(max(matris))</code> yazmak yerine <code>max(matris(:))</code> yazmak çok daha okunabilir ve profesyoneldir.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>skor_matrisi = zeros(m + 1, n + 1);</code> : Matris sıfırlarla oluşturulur. Needleman-Wunsch'tan farklı olarak, ilk satır ve ilk sütuna eksi cezalar atayan (Initialization) döngüleri YAZMIYORUZ. Buralar 0 kalmalıdır ki yerel hizalama dizinin herhangi bir noktasından cezasız başlayabilsin.</li>
        <li><code>maksimum_skor = 0;</code> : Matrisin rastgele bir yerinde ortaya çıkacak olan o devasa lokal adacığın zirve puanını kaydetmek için sayaç başlatılır.</li>
        <li><code>for i = 2:m+1</code> ve <code>for j = 2:n+1</code> : DP matrisi taranır. Eşleşme (Match) ve eşleşmeme (Mismatch) puanları <code>s</code> değişkenine atanır.</li>
        <li>Üç klasik yol (Çapraz, Üst, Sol) önceki hücrelerin mevcut skorlarına ceza veya ödül eklenerek hesaplanır.</li>
        <li><strong><code>hucre_skoru = max([yol_capraz, yol_ust, yol_sol, 0]);</code></strong> : İşte Smith-Waterman algoritmasının kalbi burasıdır. Eğer hesaplanan tüm yollar (örn: -2, -5, -4) ise, <code>max()</code> fonksiyonu bu dizideki 0'ı seçecek ve hücrenin değerini sıfırlayacaktır.</li>
        <li><code>if hucre_skoru > maksimum_skor</code> : Her bir hücre hesaplandıktan hemen sonra \"Bu sayı şimdiye kadar gördüğüm en büyük sayı mı?\" diye sorulur ve gerekirse <code>maksimum_skor</code> güncellenir.</li>
        <li>Döngü biter. Eğer bu işlemden sonra Geri İzleme (Traceback) yapılacak olsaydı, işleme sağ alt köşeden değil, tam olarak bu <code>maksimum_skor</code>'un bulunduğu hücreden başlanır ve skor 0 olana kadar geriye gidilirdi.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a5", "level": "advanced",
        "title": "5. Global Hizalamada Geri İzleme (Traceback) ile DNA Dizgisi (String) Üretimi",
        "description": "<p>Needleman-Wunsch matrisi doldurulduktan sonra, sağ alt köşeden (M,N) sol üst köşeye (0,0) doğru geri izleme (Traceback) işlemi yapılır. Sadece yönleri bulmakla kalmayıp, elde edilen yönlere göre aralara boşluk ('-') ekleyerek nihai hizalanmış iki DNA dizgisini (Hizalama Çıktısını) oluşturan kodu yazın.</p><br/><p><b>Girdi:</b> Hazır dolu bir skor matrisi ve <code>s1='GAC', s2='GC'</code></p><p><b>Beklenen Çıktı:</b><br/>G A C<br/>G - C</p>",
        "starter_code": "s1 = 'GAC';\ns2 = 'GC';\n% Basitleştirilmiş hazır matris (GAC ve GC hizalaması)\nmatris = [\n     0    -2    -4\n    -2     1    -1\n    -4    -1    -1\n    -6    -3     0];\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "s1 = 'GAC';\ns2 = 'GC';\nmatris = [0, -2, -4; -2, 1, -1; -4, -1, -1; -6, -3, 0];\nmatch = 1; mis = -1; gap = -2;\n\ni = length(s1) + 1;\nj = length(s2) + 1;\nhizali_s1 = '';\nhizali_s2 = '';\n\nwhile i > 1 || j > 1\n    if i > 1 && j > 1\n        if s1(i-1) == s2(j-1)\n            s = match;\n        else\n            s = mis;\n        end\n        \n        if matris(i, j) == matris(i-1, j-1) + s\n            % Çaprazdan geldi (Match/Mismatch)\n            hizali_s1 = [s1(i-1), hizali_s1];\n            hizali_s2 = [s2(j-1), hizali_s2];\n            i = i - 1;\n            j = j - 1;\n            continue;\n        end\n    end\n    \n    if i > 1 && matris(i, j) == matris(i-1, j) + gap\n        % Üstten geldi (s2'ye boşluk)\n        hizali_s1 = [s1(i-1), hizali_s1];\n        hizali_s2 = ['-', hizali_s2];\n        i = i - 1;\n        continue;\n    end\n    \n    if j > 1 && matris(i, j) == matris(i, j-1) + gap\n        % Soldan geldi (s1'e boşluk)\n        hizali_s1 = ['-', hizali_s1];\n        hizali_s2 = [s2(j-1), hizali_s2];\n        j = j - 1;\n    end\nend\n\ndisp('Hizalama Sonucu:');\ndisp(hizali_s1);\ndisp(hizali_s2);",
        "expected_output": "Hizalama Sonucu:\nGAC\nG-C",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Sequence Alignment ve Gaps)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte iki dizinin hizalanması sadece bir \"benzerlik skoru\" bulmaktan ibaret değildir. Araştırmacılar, mutasyonların veya delesyonların tam olarak hangi nükleotid konumlarında (lokasyonlarında) gerçekleştiğini gözleriyle görmek isterler. Bunun için dizilerin yan yana getirilmesi ve eksik olan yerlere boşluk karakteri (Genellikle Tire '-' sembolü) eklenerek aralarının açılması gerekir.</p>
        <p>Dinamik programlama matrisi doldurulduktan sonra, en sağ alt köşeden (matrisin bitişinden) başlanarak sol üst köşeye (başlangıca) doğru geriye doğru bir yol izlenir. Bu işleme <strong>Geri İzleme (Traceback)</strong> denir. Geri izleme sırasında seçilen yön, dizilerin kaderini belirler: Çapraz yön, iki harfin alt alta hizalandığını; Üst yön, birinci diziden bir harf alınırken ikinci diziye boşluk konulduğunu; Sol yön ise tam tersini ifade eder. Bu rotayı takip ederek biyologların literatürde gördüğü standart hizalama (Alignment) metinleri üretilir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize önceden doğru kurallarla doldurulmuş bir Needleman-Wunsch matrisi verilmiştir. İki adet boş karakter dizisi (<code>hizali_s1</code> ve <code>hizali_s2</code>) oluşturmalıyız. Matrisin sağ alt köşesi olan <code>(i,j)</code> koordinatından başlayarak, bulunduğumuz hücrenin değerine nasıl ulaşıldığını (Çaprazdan mı, Üstten mi, Soldan mı) geriye dönük matematiksel kontrollerle tespit etmeliyiz. Eğer çaprazsa, her iki stringin de BAŞINA ilgili harfleri ekleyip çapraz hücreye gitmeliyiz. Eğer üst veya sol ise, stringlerin birine harfi diğerine boşluğu ('-') eklemeli ve ilgili hücreye geçmeliyiz. Her iki indeks de 1 olana kadar (sol üst köşeye varana kadar) bu döngü devam etmelidir.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Geri izleme işlemi için For döngüsü kullanılamaz, çünkü For döngüsü matris içinde çapraz, dikey veya yatay gibi asimetrik adımlar atamaz. Bunun yerine şart sağlandığı sürece dönen <strong>While döngüsü</strong> kullanılır. <code>while i > 1 || j > 1</code> şartı, indekslerin matris sınırları içinde (ilklendirme satırı/sütunu olan 1'e kadar) kalmasını sağlar.</p>
        <p>Ayrıca diziyi sondan başa doğru oluşturduğumuz için, MATLAB'da bulduğumuz karakteri dizinin <strong>başına</strong> eklemeliyiz (Prepend). Bunu <code>dizi = [yeni_harf, dizi]</code> şeklinde yaparız. Alternatif olarak diziyi normal şekilde (sonuna ekleyerek) oluşturup en sonunda <code>reverse()</code> fonksiyonu ile tersine çevirmek de sık kullanılan bir tekniktir.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da bir While döngüsü içinde <code>continue</code> anahtar kelimesini kullanmak çok etkilidir. Eğer çaprazdan gelme ihtimalini test edip doğru bulursak, stringleri güncelleyip <code>continue</code> deriz. Bu, döngünün o anki turunu hemen bitirir ve aşağıdaki Üst veya Sol testlerine bakmadan doğrudan yeni döngü turuna (yeni hücreye) geçmesini sağlar.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>i = length(s1) + 1; j = length(s2) + 1;</code> : Başlangıç koordinatımızı matrisin en sağ alt köşesine (M+1, N+1) ayarlıyoruz.</li>
        <li><code>while i > 1 || j > 1</code> : En az bir indeksimiz 1'den büyük olduğu sürece (sol üst köşeye varana kadar) döngü çalışacaktır.</li>
        <li><code>if i > 1 && j > 1</code> : Her iki yöne de gitme payımız varsa önce çapraz yönü (Eşleşme/Mismatch) kontrol ederiz.</li>
        <li><code>if matris(i, j) == matris(i-1, j-1) + s</code> : Bulunduğumuz hücredeki değer, çaprazdaki hücrenin üzerine s (Match/Mismatch) eklenmesiyle Mİ elde edilmiş? Eğer eşitlik sağlanırsa evet.</li>
        <li><code>hizali_s1 = [s1(i-1), hizali_s1];</code> : Eşitlik sağlandıysa her iki harfi de (boşluksuz) kendi dizisinin başına ekleriz ve indekslerimizi (i=i-1, j=j-1) güncelleyerek çapraz hücreye taşınırız.</li>
        <li>Eğer çaprazdan gelinmemişse, <code>if matris(i, j) == matris(i-1, j) + gap</code> ile üstten mi gelindiği kontrol edilir. Eğer üstten gelinmişse (i azaldığı için) s1'e harf eklenir, s2'ye ise boşluk ('-') eklenir.</li>
        <li>Benzer şekilde soldan gelinip gelinmediği kontrol edilir. İşlem bittiğinde hizalanmış ve aralarına boşluk serpiştirilmiş mükemmel iki sekansımız (hizali_s1 ve hizali_s2) elde edilir.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a6", "level": "advanced",
        "title": "6. UPGMA Ağaç Oluşturma: Düğüm Birleştirme (Clustering)",
        "description": "<p>Önceki problemde oluşturduğumuz UPGMA Uzaklık Matrisindeki en küçük değeri (en yakın iki akrabayı) bularak, bu iki türü tek bir evrimsel düğüm (Node / Cluster) altında birleştiren algoritmanın ilk iterasyonunu yazın.</p><br/><p><b>Girdi:</b> Bir Uzaklık Matrisi (Ana köşegenler 0)</p><p><b>Beklenen Çıktı:</b> En yakın iki türün indeksleri ve aralarındaki mesafe. Örn: 'Tür 1 ve Tür 2 birleşti, Mesafe: 0.25'</p>",
        "starter_code": "matris = [\n    0     0.25  0.75;\n    0.25  0     0.50;\n    0.75  0.50  0];\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "matris = [0, 0.25, 0.75; 0.25, 0, 0.50; 0.75, 0.50, 0];\nn = size(matris, 1);\n\n% Sıfır olan köşegenleri yoksaymak için onlara devasa bir değer atıyoruz\n% Çünkü minimumu ararken 0'ları (kendisiyle uzaklığı) bulmak istemiyoruz\nkopya_matris = matris;\nfor i = 1:n\n    kopya_matris(i,i) = Inf; % Sonsuzluk\nend\n\n% Matristeki en küçük değeri bulma\nmin_deger = Inf;\nmin_satir = -1;\nmin_sutun = -1;\n\nfor i = 1:n\n    for j = 1:n\n        if kopya_matris(i,j) < min_deger\n            min_deger = kopya_matris(i,j);\n            min_satir = i;\n            min_sutun = j;\n        end\n    end\nend\n\n% Simetrik olduğu için (örn 1 ve 2 veya 2 ve 1), isimleri sıralı veriyoruz\ntur_A = min(min_satir, min_sutun);\ntur_B = max(min_satir, min_sutun);\n\nfprintf('UPGMA İlk Düğüm: Tür %d ve Tür %d birleşti.\\n', tur_A, tur_B);\nfprintf('Düğümün dallanma yüksekliği (Mesafe / 2): %.3f\\n', min_deger / 2);",
        "expected_output": "UPGMA İlk Düğüm: Tür 1 ve Tür 2 birleşti.\nDüğümün dallanma yüksekliği (Mesafe / 2): 0.125",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (Hiyerarşik Kümeleme ve Evrimsel Düğümler)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>UPGMA (Unweighted Pair Group Method with Arithmetic Mean) algoritması ile Filogenetik Ağaç çiziminin ilk şartı Uzaklık Matrisini oluşturmaktır. Matris hazır olduktan sonra süreç, <strong>Agglomerative Hierarchical Clustering (Aşağıdan Yukarıya Hiyerarşik Kümeleme)</strong> mantığıyla işler. Başlangıçta her tür (İnsan, Fare, Şempanze vb.) kendi başına bağımsız bir yapraktır (Leaf). Algoritma matrise bakar ve aralarındaki mesafe (farklılık) en küçük olan iki türü bulur. Bu iki tür, evrimsel olarak birbirine en yakın akrabadır. Algoritma bu iki türü alır ve onları evrim ağacında tek bir dalda birleştirir (Yeni bir Node / Düğüm oluşturur).</p>
        <p>Bu yeni düğüm oluştuktan sonra, eski iki tür silinir ve yerlerine bu birleşik \"Grup (Cluster)\" matrise yeni bir satır/sütun olarak eklenir. Grubun diğer türlerle olan mesafesi, eski iki türün mesafelerinin aritmetik ortalaması alınarak hesaplanır. Bu süreç, matriste tek bir eleman kalana (Ağacın kökü - Root Node bulunana) kadar tekrarlanır. Bu problemde UPGMA algoritmasının bu döngüsel kalbini, yani en yakın akrabaları bulup onları birleştiren ilk iterasyonu kodlayacağız. Ağaç çizimlerinde dal (branch) uzunluğu, iki tür arasındaki toplam mesafenin yarısıdır (Mesafe / 2).</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Elimizde içi sayılarla dolu iki boyutlu bir matris var. Bizden istenen bu matrisin içindeki mutlak en küçük sayıyı bulmak ve bu sayının hangi satır ve sütunda (hangi iki tür arasında) olduğunu ekrana yazdırmaktır. Ancak burada çok büyük bir tuzak vardır: Mesafe matrislerinin ana köşegeni (Diagonal), yani türlerin kendileriyle olan mesafesi (Tür 1 ile Tür 1 arası) doğal olarak daima 0'dır. Eğer direkt matriste minimum ararsak, her zaman 0 buluruz ve algoritma Tür 1'i kendisiyle birleştirmeye çalışır. Amacımız bu sıfırları göz ardı ederek, farklı türler arasındaki en küçük sayıyı bulmaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Köşegendeki sıfırlardan kurtulmanın en zarif yolu, matrisin bir kopyasını alıp köşegenlere bilgisayarın algılayabileceği en büyük sayıyı atamaktır. MATLAB'da bu özel sayı <code>Inf</code> (Infinity - Sonsuzluk) olarak tanımlıdır. Eğer bir hücreye Inf atarsanız, o hücre minimum arama yarışından sonsuza dek elenmiş olur. Bunun yerine döngü içinde <code>if i ~= j</code> sorgusu da yapılabilir, ancak büyük matrislerde her iterasyonda mantıksal kontrol yapmak işlemciyi yorar; veriyi önceden (Inf ile) zehirlemek çok daha hızlı bir vektörel optimizasyondur.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> MATLAB'da bir matrisin köşegenini değiştirmek için döngü kullanmak yerine <code>kopya_matris(logical(eye(n))) = Inf;</code> gibi ileri düzey bir Vektörel İndeksleme kullanılabilir. <code>eye()</code> fonksiyonu kimlik matrisi (sadece köşegeni 1 olan matris) üretir ve bunu mantıksal maske olarak kullanmak tek satırda tüm köşegeni günceller.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>kopya_matris = matris;</code> : Orijinal veriyi bozmamak için matrisin kopyasını alıyoruz.</li>
        <li><code>for i = 1:n ... kopya_matris(i,i) = Inf;</code> : Matrisin ana köşegeninde (i=j olan yerler) bulunan tüm sıfırları sonsuzlukla (Inf) değiştiriyoruz. Böylece algoritmamız bu hücreleri bir daha asla \"en küçük değer\" olarak seçmeyecek.</li>
        <li><code>min_deger = Inf; min_satir = -1; min_sutun = -1;</code> : Minimum bulma algoritmalarının standart başlangıcıdır. Aranacak sayıyı en baştan çok büyük tutarız ki karşılaştığı ilk gerçek sayı (örn: 0.75), Inf'ten küçük olduğu için hemen tahta otursun.</li>
        <li><code>for i... for j... if kopya_matris(i,j) < min_deger</code> : İç içe geçmiş döngülerle tüm hücreleri geziyor ve eğer o hücredeki sayı, şu ana kadar gördüğümüz en küçük sayıdan da küçükse <code>min_deger</code> değişkenimizi bu yeni sayıyla güncelliyoruz. Ayrıca bu hücrenin koordinatlarını (i ve j) kaydediyoruz.</li>
        <li><code>tur_A = min(min_satir, min_sutun);</code> : Matris simetrik olduğu için bulduğumuz sonuç 2. satır, 1. sütun olabilir. Çıktıda \"Tür 2 ve Tür 1\" yazması yerine sayısal bir düzen (Tür 1 ve Tür 2) olması için küçük ve büyük indeksleri sıralıyoruz.</li>
        <li>Son olarak birleştirilen türleri ve filogenetik ağaçtaki dal (branch) yüksekliğini temsil eden \"Mesafe / 2\" değerini <code>fprintf</code> ile ekrana basıyoruz.</li>
    </ul>
</div>
        """
    },
    {
        "id": "a7", "level": "advanced",
        "title": "7. Saklı Markov Modelleri (HMM): Forward Algoritması (Toplam Olasılık)",
        "description": "<p>Viterbi algoritması en muhtemel tek bir yolu bulurken, Forward Algoritması o diziyi (Gözlemi) üretebilecek Olası Tüm Yolların (All Possible Paths) ihtimallerinin toplamını bulur. Bir DNA dizisinin verilen HMM modeli tarafından üretilme olasılığını hesaplayan Forward algoritmasını kodlayın.</p><br/><p><b>Girdi:</b> <code>dna='AT'</code> (Sadece iki harf)</p><p><b>Beklenen Çıktı:</b> <code>Toplam Olasılık: 0.1600</code></p>",
        "starter_code": "dna = 'AT';\n\n% Model Olasılıkları\np_emit_N = containers.Map({'A','T','C','G'}, [0.4, 0.4, 0.1, 0.1]);\np_emit_I = containers.Map({'A','T','C','G'}, [0.1, 0.1, 0.4, 0.4]);\np_trans_NN = 0.8; p_trans_NI = 0.2;\np_trans_II = 0.8; p_trans_IN = 0.2;\n\n% Kodunuzu buraya yazın\n\n",
        "solution_code": "dna = 'AT';\np_emit_N = containers.Map({'A','T','C','G'}, [0.4, 0.4, 0.1, 0.1]);\np_emit_I = containers.Map({'A','T','C','G'}, [0.1, 0.1, 0.4, 0.4]);\np_trans_NN = 0.8; p_trans_NI = 0.2;\np_trans_II = 0.8; p_trans_IN = 0.2;\n\nfwd_N = zeros(1, length(dna));\nfwd_I = zeros(1, length(dna));\n\n% Başlangıç ihtimalleri (%50 - %50)\nfwd_N(1) = 0.5 * p_emit_N(dna(1));\nfwd_I(1) = 0.5 * p_emit_I(dna(1));\n\n% Forward iterasyonu\nfor t = 2:length(dna)\n    harf = dna(t);\n    \n    % Viterbi'deki MAX yerine SUM (Toplama) kullanılır\n    yol1_N = fwd_N(t-1) * p_trans_NN * p_emit_N(harf);\n    yol2_N = fwd_I(t-1) * p_trans_IN * p_emit_N(harf);\n    fwd_N(t) = yol1_N + yol2_N;\n    \n    yol1_I = fwd_N(t-1) * p_trans_NI * p_emit_I(harf);\n    yol2_I = fwd_I(t-1) * p_trans_II * p_emit_I(harf);\n    fwd_I(t) = yol1_I + yol2_I;\nend\n\n% En sonunda iki durumun ihtimalleri toplanır\ntoplam_olasilik = fwd_N(end) + fwd_I(end);\nfprintf('Gözlemin Toplam Olasılığı: %.4f\\n', toplam_olasilik);",
        "expected_output": "Gözlemin Toplam Olasılığı: 0.1600",
        "explanation": """
<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">📖 Teorik Temel: Biyolojik Arka Plan (HMM Forward Algoritması)</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Biyoinformatikte Gizli Markov Modelleri (HMM) ile üç temel soru cevaplanır. 1) Verilen dizi hangi gizli durumlardan geçti? (Çözüm: Viterbi Algoritması). 2) Verilen diziye bakarak modelimizin parametrelerini (olasılıklarını) nasıl daha iyi eğitiriz? (Çözüm: Baum-Welch Algoritması). 3) Elimizdeki bu DNA dizisinin, kurduğumuz bu spesifik modele ait olma ihtimali nedir? (Çözüm: Forward Algoritması).</p>
        <p>Forward algoritmasının biyolojik kullanımı şöyledir: Diyelim ki elinizde bilinmeyen bir protein dizisi var. Pfam veritabanında ise binlerce farklı protein ailesinin HMM modelleri var (Kinaz modeli, Helikaz modeli vb.). Bu diziyi Kinaz modeline verirsiniz, size %1 ihtimal (0.01) verir. Helikaz modeline verirsiniz, %80 ihtimal (0.8) verir. Böylece dizinin bir helikaz olduğunu çok yüksek bir matematiksel güvenle sınıflandırırsınız (Sequence Classification). Viterbi algoritması bize o diziyi üretebilecek tek bir <strong>\"En İyi Yolu\"</strong> verir. Ancak Forward algoritması, o diziyi üretebilecek <strong>\"Tüm Olası Yolların\" ihtimallerinin toplamını</strong> verir. Bir dizinin modele ait olma ihtimalini hesaplarken tüm kombinasyonların katkısı hesaba katılmalıdır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🎯 Problemin Tanımı ve Amacı</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Bize sadece 'AT' dizisi verilmiştir. 2 harf için 4 farklı gizli durum senaryosu vardır: NN, NI, IN, II. Yani 'A' harfi N bölgesinden, 'T' harfi N bölgesinden gelmiş olabilir (NN). Ya da A harfi N'den, T harfi I bölgesinden gelmiş olabilir (NI). Bizden istenen, bu 4 farklı ihtimal yolunun herbirinin matematiksel olasılığını bulmak ve Hepsini Birbiriyle Toplayarak dizinin tüm olasılık uzayındaki (Probability space) toplam ağırlığını (Likelihood) hesaplamaktır.</p>
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">💻 MATLAB Yaklaşımı ve İleri Düzey Algoritma Optimizasyonu</h4>
    <div style="margin-top: 1rem; line-height: 1.8;">
        <p>Eğer tüm yolları (Kombinasyonları) tek tek for döngüleriyle hesaplamaya kalkarsak, dizi uzadıkça olasılık yolları üstel (Exponential, 2^N) olarak artar ve bilgisayar çöker. Dinamik Programlama (Forward algoritması) burada hayat kurtarır. Viterbi kodundan yapısal olarak neredeyse hiçbir farkı yoktur. İki algoritma arasındaki tek matematiksel fark şudur: Viterbi, geçmişten gelen iki yoldan (Örn NN ve IN) hangisi büyükse onu seçerdi (<code>max(NN, IN)</code>). Forward algoritması ise geçmişi unutmaz, iki yolu da birbirine toplayarak ilerler (<code>NN + IN</code>). Bu basit <strong>MAX -> SUM</strong> (Maksimum yerine Toplam) değişimi, eksponansiyel karmaşıklığı doğrusal (Linear, O(N)) hale getirir.</p>
    </div>
    <div class="highlight-box" style="margin-top: 1rem;">
        <strong>💡 Programlama İpucu:</strong> Tıpkı Viterbi'de olduğu gibi, Forward algoritmasında da sayılar sürekli olarak birbiriyle çarpıldığı için milyonlarca adımlık dizilerde sonuç 0.0000001 gibi değerlere inerek Underflow (alt taşma) hatasına yol açar. Bu yüzden gerçek sistemler, her adımda vektörü 1'e tamamlayacak şekilde ölçeklendiren (Scaling) ek matematiksel prosedürler uygularlar.
    </div>
</div>

<div class="textbook-section">
    <h4 style="color: var(--primary); margin-top: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">🔍 Adım Adım Kod Analizi ve Matematiksel Mantık</h4>
    <ul style="margin-top: 1rem; line-height: 1.8;">
        <li><code>fwd_N</code> ve <code>fwd_I</code> : Her adımda olasılıkların toplamını biriktireceğimiz yatay vektörlerimiz.</li>
        <li><strong>Başlangıç:</strong> Birinci harf ('A') için hesap yapılır. (0.5 * 0.4 = 0.2 N için), (0.5 * 0.1 = 0.05 I için).</li>
        <li><strong>Döngü (t=2 için):</strong> İkinci harf ('T') işleme alınır.</li>
        <li><code>yol1_N</code> : NN yolunun ihtimalidir. Geçmişin N ihtimali (0.2) x N->N Geçişi (0.8) x N'nin T üretme ihtimali (0.4) = 0.064</li>
        <li><code>yol2_N</code> : IN yolunun ihtimalidir. Geçmişin I ihtimali (0.05) x I->N Geçişi (0.2) x N'nin T üretme ihtimali (0.4) = 0.004</li>
        <li><code>fwd_N(t) = yol1_N + yol2_N;</code> : Viterbi'de 0.064'ü seçerdik. Ancak burada <strong>Toplam Olasılık</strong> aradığımız için ikisini topluyoruz (0.064 + 0.004 = 0.068). N noktasında bulunma ihtimalimiz artık 0.068'dir.</li>
        <li>Aynı toplama işlemleri I (Island) durumuna giden yollar (NI ve II) için de uygulanır (Sonuç: 0.008 + 0.004 = 0.012).</li>
        <li>Döngü bittikten sonra, dizinin en sonundaki ihtimaller (0.068 ve 0.012) birbirine toplanır (0.080) ve bu modelin 'AT' dizisini üretme toplam olasılığı (Total Likelihood) elde edilir.</li>
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
