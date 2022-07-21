class GPWHomePage:

    def __int__(self, driver):
        self.driver = driver
        self.input_shear_name = "/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input"

    def find_shear(self):
        self.driver.find_elament(By.XPATH, self.input_shear_name)