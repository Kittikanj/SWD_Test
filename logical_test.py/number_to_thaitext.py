class Solution(): 
    def number_to_thaitext(self,number):
    
        if number < 0 or number >= 10000000:
            return "Invalid number"
        
        thai = {0:"ศูนย์", 
                1:"หนึ่ง", 
                2:"สอง", 
                3:"สาม", 
                4:"สี่", 
                5:"ห้า", 
                6:"หก", 
                7:"เจ็ด", 
                8:"แปด", 
                9:"เก้า"}
        
        unit = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
    
        if number == 0:
            return thai[0]

        thai_text = ""
        i = 0
        while number > 0:
            digit = number % 10
            if i == 1 and digit == 2:
                thai_text = "ยี่สิบ" + thai_text
            elif i == 1 and digit == 1:
                thai_text = "สิบ" + thai_text
            elif i > 1 and digit == 1 and number // 10 % 10 != 0:
                thai_text = "เอ็ด" + unit[i] + thai_text
            elif digit != 0:
                thai_text = thai[digit] + unit[i] + thai_text
            number //= 10
            i += 1

        return thai_text