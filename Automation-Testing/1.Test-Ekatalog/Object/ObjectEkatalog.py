from playwright.sync_api import Page, expect

class Ekatalog_v1 :

    def __init__(self, page : Page) :
        self.page = page
       
    def open_ekatalog(self) :
        expect(self.page.get_by_text("Tanggal")).to_be_visible()
        with self.page.expect_popup() as new_tab :
            self.page.locator('a[href="sso/ekatalog"]').click()

            self.ekatalog_tab = new_tab.value  
        
            expect(self.ekatalog_tab.get_by_text("Produk")).to_be_visible
            self.ekatalog_tab.get_by_text("Gearbox Hoist Heavy Duty Crane Pelabuhan 5 Ton").click()

    def cost_center(self) : 
        self.ekatalog_tab.get_by_placeholder("Pilih Cost Center...").click()
        self.ekatalog_tab.get_by_placeholder("Pilih Cost Center...").fill("Departemen Pengadaan (2030105511)")
        expect(self.ekatalog_tab.get_by_placeholder("Pilih Cost Center")).to_be_visible()
        # get_by_role("option",name= "Departemen Pengadaan (2030105511)").click()

    def gl_account(self) :
        self.ekatalog_tab.get_by_placeholder("Pilih GL Account...").click()
        self.ekatalog_tab.get_by_placeholder("Pilih GL Account...").fill("Beban SDPK Sharing Revenue Pelindo Grup (Afiliasi) (5061300000)")

    def plant(self) : 
        self.ekatalog_tab.locator("select").select_option("1")

    def quantity(self,jumlah) : 
        for _ in range(jumlah) :
            self.ekatalog_tab.locator('button:has(svg.lucide-plus)').click()

    def check_out(self) :
        self.ekatalog_tab.get_by_role("button",name="Check Budget").click()
        self.ekatalog_tab.get_by_role("button",name="Tutup").click()
        self.ekatalog_tab.get_by_role("button",name="Beli Sekarang").click()

    def preview_co(self) : 
        expect(self.ekatalog_tab).to_have_url("https://e-katalog-dev.*********/ekatalog/checkout-preview")
        ## Account
        self.ekatalog_tab.locator("label").filter(has_text="Account Assignment").locator("..").locator("select").select_option("K")
        self.ekatalog_tab.locator("label").filter(has_text="Item Category").locator("..").locator("select").select_option("B")
        self.ekatalog_tab.locator("label").filter(has_text="Delivery Date").locator("..").locator("input[type='date']").fill("2026-09-01")
        
        ## Purchase
        self.ekatalog_tab.get_by_role("button",name="Purchase").click()
        self.ekatalog_tab.locator("label").filter(has_text="Purchase Group").locator("..").locator("select").select_option("002")

        ## Financial
        self.ekatalog_tab.get_by_role("button",name="Financial").click()

        ## Informasi Pengiriman 
        self.ekatalog_tab.locator("label").filter(has_text="Alamat Pengiriman").locator("..").locator("select").select_option("5")
        self.ekatalog_tab.locator("label").filter(has_text="Tipe Pengiriman").locator("..").locator("select").select_option("DIKIRIM_SELLER")

        ## Detail PR
        ## 1. Dokumen
        self.ekatalog_tab.get_by_role("button",name="Tambah Dokumen").click()
        self.ekatalog_tab.get_by_placeholder("Masukkan nama dokumen").fill("Dokumen Testing PR Ekatalog")
        self.ekatalog_tab.locator("input[placeholder='Masukkan keterangan']").fill("Testing Dokumen PR")
        self.ekatalog_tab.locator("#file-upload").set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")
        self.ekatalog_tab.get_by_role("button",name="Simpan").click()

        ## 2. Informasi Approval
        self.ekatalog_tab.get_by_role("button",name="Informasi Approval").click()
        self.ekatalog_tab.locator("label").filter(has_text="Document Type").locator("..").locator("select").select_option("ZPR5")
        self.ekatalog_tab.locator("label").filter(has_text="Requestioner").locator("..").locator("select").select_option("Z24001") 
        self.ekatalog_tab.locator("tr").filter(has_text='9999901').locator("input[type='Email']").fill("pelindoeproc@gmail.com")   
        self.ekatalog_tab.locator("tr").filter(has_text='9999902').locator("input[type='Email']").fill("t93815576@gmail.com")     

        ## Detail PO
        self.ekatalog_tab.locator("label").filter(has_text="Doc Type").locator("..").locator("select").select_option("ZP12")
        self.ekatalog_tab.locator("label").filter(has_text="Validity Start").locator("..").locator("input[type='date']").fill("2026-08-26")
        self.ekatalog_tab.locator("label").filter(has_text="Validity End").locator("..").locator("input[type='date']").fill("2026-08-28")
        self.ekatalog_tab.locator("textarea[placeholder='Masukkan keterangan']").fill("Testing PO Ekatalog")
        self.ekatalog_tab.locator("table").filter(has_text="LEVEL").locator("tr").filter(has_text="2").locator("input[type='Email']").fill("pelindoeproc@gmail.com")

        ## Checkout
        self.ekatalog_tab.get_by_role("button",name="Checkout").click()
        expect(self.ekatalog_tab.get_by_text("Konfirmasi Checkout")).to_be_visible()
        self.ekatalog_tab.get_by_role("button",name="Ya, Checkout").click()
        self.ekatalog_tab.get_by_role("button",name="Buat Pesanan").click()
        self.ekatalog_tab.get_by_role("button",name="Ya, Buat Pesanan").click()

    def menu_pesanan_penyedia(self) :
        self.ekatalog_tab.get_by_role("button", name="Pesanan").click()
        self.ekatalog_tab.get_by_role("link",name="Konfirmasi Pesanan - Penyedia").click()
    
    def confirmation_product (self) :
        row_confirm_pesanan = self.ekatalog_tab.locator("tr").filter(has_text="ORD-20260902140649699-6303-003E5A17")
        row_confirm_pesanan.get_by_role("button",name="Aksi").click()
        self.ekatalog_tab.get_by_role("button",name="Lihat Detail").click()

    def form_confirm_product(self) :
        self.ekatalog_tab.get_by_role("button",name="Tambah Item").click()
        expect(self.ekatalog_tab.get_by_text("Tambah Detail Harga")).to_be_visible()
        self.ekatalog_tab.get_by_placeholder("Contoh: Biaya Pengiriman, Asuransi").fill("Biayan Pengiriman Produk")
        self.ekatalog_tab.get_by_placeholder("Masukkan keterangan (opsional)").fill("Testing")
        self.ekatalog_tab.get_by_placeholder("Contoh: Kg, Liter, Meter, Buah").fill("Kg")
        self.ekatalog_tab.locator("label").filter(has_text="Berat").locator("..").locator("input").fill("10")
        self.ekatalog_tab.locator("label").filter(has_text="Harga").locator("..").locator("input").fill("1000000")
        self.ekatalog_tab.get_by_role("button",name="Simpan").click()
        self.ekatalog_tab.get_by_role("button",name="Konfirmasi").click()
        self.ekatalog_tab.get_by_role("button",name="Ya, Konfirmasi").click()

    def pembelian_prpo(self) :
        self.ekatalog_tab.get_by_role("button",name="Pembelian").click()
        self.ekatalog_tab.get_by_role("link",name="Daftar Pembelian").click()
        row_prpr = self.ekatalog_tab.locator("tr").filter(has_text="ORD-20260902140649699-6303-003E5A17")
        row_prpr.get_by_role("link",name="Detail").click()

    def posting_prpo(self) :
        self.ekatalog_tab.get_by_role("button",name="Posting").click()

    def delivery_list (self) :
        self.ekatalog_tab.get_by_role("button",name="Pesanan").click()
        self.ekatalog_tab.get_by_role("link",name="Daftar Pesanan").click()
        row_delivery = self.ekatalog_tab.locator("tr").filter(has_text="7400000021")
        row_delivery.get_by_role("button",name="Detail").click()

    def delivery_product(self) : 
        self.ekatalog_tab.get_by_role("button",name="Informasi Pengiriman").click()
        self.ekatalog_tab.get_by_role("link",name="Tambah Pengiriman").click()

        ## Form Surat Jalan
        self.ekatalog_tab.locator("input[type='datetime-local']").fill("2026-09-02T16:00")
        self.ekatalog_tab.get_by_placeholder("Masukkan nomor kendaraan").fill("B 7281 BAC")
        self.ekatalog_tab.get_by_placeholder("Masukkan nomor surat jalan").fill("IDN-0002-PNGRM-EKTLG-PLND")
        self.ekatalog_tab.get_by_placeholder("Masukkan judul surat jalan").fill("Pengiriman Produk Gearbox Hoist")
        self.ekatalog_tab.locator("label").filter(has_text="Cost Center").locator("..").locator("select").select_option("916")

        ## Dokumen Pengiriman 
        self.ekatalog_tab.get_by_role("button",name="Tambah Dokumen").click()
        self.ekatalog_tab.get_by_placeholder("Masukkan nama dokumen").fill("Dokumen Pengiriman Produk Gearbox Hoist")
        self.ekatalog_tab.get_by_role("textbox",name="Masukkan keterangan").fill("Testing Dokumen Pengiriman")
        self.ekatalog_tab.locator("#dokumen-file-upload").set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")
        modal_1= self.ekatalog_tab.locator("div.bg-white.rounded-2xl.shadow-xl").filter(has=self.ekatalog_tab.get_by_role("heading",name="Tambah Dokumen"))
        modal_1.get_by_role("button",name="Simpan").click()

        ## Approval Pengiriman
        ## Penanda Tangan
        self.ekatalog_tab.get_by_role("button",name="Tambah Approval").click()
        self.ekatalog_tab.locator("label").filter(has_text="Tipe").locator("..").locator("select").select_option("PENANDA TANGAN")
        self.ekatalog_tab.get_by_placeholder("Ketik untuk mencari NIPP atau Nama...").fill("19")
        self.ekatalog_tab.get_by_placeholder("Masukkan email").fill("pelindoeproc@gmail.com")
        modal_2 = self.ekatalog_tab.locator("div.bg-white.rounded-2xl.shadow-xl").filter(has=self.ekatalog_tab.get_by_role("heading",name="Tambah Approval"))
        modal_2.get_by_role("button",name="Simpan").click()

        ## Driver
        self.ekatalog_tab.get_by_role("button",name="Tambah Approval").click()
        self.ekatalog_tab.locator("label").filter(has_text="Tipe").locator("..").locator("select").select_option("DRIVER")
        self.ekatalog_tab.get_by_placeholder("Masukkan nama").fill("Core")
        self.ekatalog_tab.get_by_placeholder("Masukkan jabatan").fill("Koordinator Driver")
        self.ekatalog_tab.get_by_placeholder("Masukkan email").fill("pelindoeproc@gmail.com")
        self.ekatalog_tab.get_by_role("spinbutton").fill("2")
        modal_2.get_by_role("button",name="Simpan").click()
        
        ## Penerima
        self.ekatalog_tab.get_by_role("button",name="Tambah Approval").click()
        self.ekatalog_tab.locator("label").filter(has_text="Tipe").locator("..").locator("select").select_option("PENERIMA")
        self.ekatalog_tab.get_by_placeholder("Ketik untuk mencari NIPP atau Nama...").fill("00009800093")
        self.ekatalog_tab.get_by_placeholder("Masukkan email").fill("pelindoeproc@gmail.com")
        self.ekatalog_tab.get_by_role("spinbutton").fill("3")
        modal_2.get_by_role("button",name="Simpan").click()

        ## Simpan Surat Jalan
        modal_3 = self.ekatalog_tab.locator("div.bg-white.rounded-2xl.shadow-xl").filter(has=self.ekatalog_tab.get_by_role("heading",name="Kelola Surat Jalan"))
        modal_3.get_by_role("button",name="Simpan").click() 
        self.ekatalog_tab.get_by_role("button",name="Preview Surat Jalan").click()     
        self.ekatalog_tab.get_by_role("button",name="Posting Surat Jalan").click()
        self.ekatalog_tab.get_by_role("button",name="Ya, Posting").click()

    def received_product(self) : 
        self.ekatalog_tab.get_by_role("button",name="Penerimaan").click()
        self.ekatalog_tab.get_by_role("link",name="Penerimaan & Pengecekan Produk").click()
        row_rp = self.ekatalog_tab.locator("tr").filter(has_text="7400000021")
        row_rp.get_by_role("link",name="Detail").click()

    def confirm_product(self) : 
        self.ekatalog_tab.get_by_role("button",name="YA").click()
        self.ekatalog_tab.get_by_role("button",name="Ya, Konfirmasi").click()

    def item_good_receipt(self) :
        self.ekatalog_tab.get_by_role("button",name="Item Good Receipt").click()
        self.ekatalog_tab.get_by_role("spinbutton").fill("3")
        self.ekatalog_tab.locator("label").filter(has_text="Spesifikasi Barang").locator("..").locator("select").select_option("Sesuai")
        self.ekatalog_tab.locator("label").filter(has_text="Kondisi Barang").locator("..").locator("select").select_option("Baik")
        self.ekatalog_tab.locator('input[type="file"]').set_input_files("D:/Project PEPROC/TEST DOKUMEN/CONTOH DOKUMEN.PDF")
        # expect(self.ekatalog_tab.get_by_text("Foto material berhasil diupload")).to_be_visible()
        self.ekatalog_tab.locator("td").filter(has_text="Serial Number").locator("input").fill("3721021")
        self.ekatalog_tab.locator("td").filter(has_text="Keterangan").locator("textarea").fill("Testing Doc")
        self.ekatalog_tab.get_by_role("button",name="Simpan").click()

    def approval_penerimaan_product(self) :
        self.ekatalog_tab.get_by_role("button",name="Approval").click()

        ## Pengguna
        row_app_pp = self.ekatalog_tab.locator("h3").filter(has_text="Daftar Pengguna")   
        row_app_pp.get_by_role("button",name="+ Tambah").click()
        self.ekatalog_tab.get_by_placeholder("Cari pegawai").fill("1891024641")
        self.ekatalog_tab.locator("h2").filter(has_text="Tambah Daftar Pengguna").get_by_role("button",name="Cari")
        expect(self.ekatalog_tab.get_by_text("1891024641"))

        ## Penyedia
        row_app_pp1 = self.ekatalog_tab.locator("label").filter(has_text="Daftar Penyedia")
        row_app_pp1.get_by_role("button",name="+ Tambah").click()
        


        