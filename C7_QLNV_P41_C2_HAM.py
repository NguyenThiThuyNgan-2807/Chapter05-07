class NVVanPhong:
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_ngay):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = self.calculate_salary(so_ngay)
        self.so_ngay = so_ngay

    def calculate_salary(self, so_ngay):
        return self.luong_co_ban * so_ngay


class NVBanHang:
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_san_pham):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = self.calculate_salary(so_san_pham)
        self.so_san_pham = so_san_pham

    def calculate_salary(self, so_san_pham):
        return self.luong_co_ban * so_san_pham


def main():
    # Khởi tạo danh sách nhân viên
    nhan_vien = [
        NVVanPhong("VP001", "Nguyễn Văn A", 3000000, 22),
        NVVanPhong("VP002", "Trần Thị B", 3200000, 20),
        NVVanPhong("VP003", "Lê Văn C", 3100000, 21),
        NVVanPhong("VP004", "Phạm Thị D", 2800000, 23),
        NVVanPhong("VP005", "Nguyễn Văn E", 3500000, 19),
        NVBanHang("BH001", "Nguyễn Văn F", 5000000, 10),
        NVBanHang("BH002", "Trần Thị G", 5500000, 15),
        NVBanHang("BH003", "Lê Văn H", 5200000, 12),
        NVBanHang("BH004", "Phạm Thị I", 5400000, 14),
        NVBanHang("BH005", "Nguyễn Văn J", 5800000, 9)
    ]

    # In thông tin nhân viên
    for nv in nhan_vien:
        if isinstance(nv, NVVanPhong):
            print(f"Nhân viên văn phòng - Mã: {nv.ma_nv}, Họ tên: {nv.ho_ten}, Lương tháng: {nv.luong_hang_thang:,}đ")
        elif isinstance(nv, NVBanHang):
            print(f"Nhân viên bán hàng - Mã: {nv.ma_nv}, Họ tên: {nv.ho_ten}, Lương tháng: {nv.luong_hang_thang:,}đ")


if __name__ == "__main__":
    main()