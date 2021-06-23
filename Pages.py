import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure


class Locators:
    LOCATOR_LOGO = (By.CSS_SELECTOR, ".col-xl-2.col-lg-2.col-md-2.col-sm-6.col-6.logo_box")
    LOCATOR_top_users_balance = (By.CSS_SELECTOR, ".mat-menu-trigger.ng-star-inserted")
    LOCATOR_top_users_balances_on_Ethereum = (By.LINK_TEXT, "Ethereum holders")
    LOCATOR_top_DAI_funds_holders = (By.LINK_TEXT, "DAI funds holders")
    LOCATOR_top_BSC_holders = (By.LINK_TEXT, "BSC holders")
    LOCATOR_top_BSC_BUSD_USDT = (By.LINK_TEXT, "BUSD+USDT funds holders")  # список холдеров
    LOCATOR_top_DFX_BUSD = (By.LINK_TEXT, "DFX-BUSD funds holders")
    LOCATOR_top_DFX = (By.LINK_TEXT, "DFX funds holders")
    LOCATOR_top_BTCB = (By.LINK_TEXT, "BTCB funds holders")
    LOCATOR_top_BUSD = (By.LINK_TEXT, "BUSD funds holders")
    LOCATOR_top_3POOL_ELIPSIS = (By.LINK_TEXT, "3POOL ELIPSIS funds holders")
    LOCATOR_top_BTCB_RENBTC = (By.LINK_TEXT, "BTCB/RENBTC funds holders")
    LOCATOR_top_3POOL_NERVE = (By.LINK_TEXT, "3POOL NERVE funds holders")
    LOCATOR_top_ETH = (By.LINK_TEXT, "ETH funds holders")
    LOCATOR_top_XRP = (By.LINK_TEXT, "XRP funds holders")
    LOCATOR_top_DOT = (By.LINK_TEXT, 'DOT funds holders')
    LOCATOR_DFX_PRICE = (By.CSS_SELECTOR, '.stat>:nth-child(3)>:nth-child(1)>:nth-child(2)')
    LOCATOR_menu = (By.XPATH, '//button[@class = "mobile_button"]')
    LOCATOR_guarantees = (By.XPATH, '//span[@class = "mat-button-wrapper"]')
    LOCATOR_balance_on_etherscan = (By.CSS_SELECTOR, '#cdk-overlay-0>:nth-child(1)>:nth-child(1)>:nth-child(1)')
    LOCATOR_check_profit = (By.CSS_SELECTOR, '#cdk-overlay-0>:nth-child(1)>:nth-child(1)>:nth-child(2)')
    LOCATOR_audit = (By.CSS_SELECTOR, '#cdk-overlay-0>:nth-child(1)>:nth-child(1)>:nth-child(3)')
    LOCATOR_git = (By.CSS_SELECTOR, '#cdk-overlay-0>:nth-child(1)>:nth-child(1)>:nth-child(4)')
    LOCATOR_how_works = (By.CSS_SELECTOR, '#cdk-overlay-0>:nth-child(1)>:nth-child(1)>:nth-child(7)')
    LOCATOR_pools = (By.LINK_TEXT, 'Pools')
    LOCATOR_wiki = (By.LINK_TEXT, 'Wiki')
    LOCATOR_airdrop = (By.LINK_TEXT, 'DFX Airdrop')
    LOCATOR_buy_DFX = (By.LINK_TEXT, 'Buy DFX')
    LOCATOR_lang = (By.XPATH, '//button[@class ="mat-menu-trigger"]')
    LOCATOR_read_article = (By.LINK_TEXT, 'Read article on')
    proof_check_locator = (By.LINK_TEXT, 'Check balance on Etherscan')
    read_audit_locator = (By.LINK_TEXT, 'Read the Security Audit')
    see_git_locator = (By.LINK_TEXT, 'See code on GitHub')
    see_guide_locator = (By.LINK_TEXT, 'See guide')
    footer_logo_LOCATOR = (By.CSS_SELECTOR, '.left>:nth-child(1)')
    footer_audit_LOCATOR = (By.ID, 'footLink_audit')
    footer_contract_LOCATOR = (By.ID, 'footLink_contract')
    footer_git_LOCATOR = (By.ID, 'footLink_github')
    footer_licence_LOCATOR = (By.ID, 'footLink_licence')
    footer_support_LOCATOR = (By.ID, 'footLink_support')
    footer_tg_LOCATOR = (By.ID, 'footLink_telegram')
    footer_medium_LOCATOR = (By.ID, 'footLink_medium')
    footer_discord_LOCATOR = (By.ID, 'footLink_discord')
    footer_twitter_LOCATOR = (By.ID, 'footLink_twitter')
    footer_fb_LOCATOR = (By.CSS_SELECTOR, '.right_part>:nth-child(3)')
    FAQ1_LOCATOR = (By.ID, 'mat-expansion-panel-header-0')
    FAQ1_git_LOCATOR = (By.ID, 'source_github')
    FAQ1_owners_eth_LOCATOR = (By.ID, 'funds_owners_eth')
    FAQ1_owners_bsc_LOCATOR = (By.ID, 'funds_owners_bsc')
    FAQ2_LOCATOR = (By.ID, 'mat-expansion-panel-header-1')
    FAQ2_article_LOCATOR = (By.ID, 'article_binance')
    FAQ3_LOCATOR = (By.ID, 'mat-expansion-panel-header-2')
    FAQ4_LOCATOR = (By.ID, 'mat-expansion-panel-header-3')
    FAQ5_LOCATOR = (By.ID, 'mat-expansion-panel-header-4')
    FAQ3_article_medium_LOCATOR = (By.LINK_TEXT, 'Article on Medium')
    FAQ4_balance_on_compound_LOCATOR = (By.LINK_TEXT, 'Balance on Compound')
    FAQ4_balance_on_eth_LOCATOR = (By.LINK_TEXT, 'Balance on Etherscan')
    FAQ4_balance_on_bsc_LOCATOR = (By.LINK_TEXT, 'Balance on BSCscan')
    FAQ5_audit_LOCATOR = (By.LINK_TEXT, 'Report from Pessimistic')
    FAQ5_instruction_LOCATOR = (By.LINK_TEXT, 'Instruction')
    FAQ5_client_LOCATOR = (By.LINK_TEXT, 'Download client')


class clicks(BasePage):
    def FAQ5(self):
        click_FAQ5 = self.find_element(Locators.FAQ5_LOCATOR)
        click_FAQ5.click()
        click_FAQ5_audit = self.find_element(Locators.FAQ5_audit_LOCATOR).click()
        self.new_window('https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf')
        click_FAQ5_instruction = self.find_element(Locators.FAQ5_instruction_LOCATOR).click()
        self.new_window('https://defirex.org/assets/data/autonome_client_instruction_en.pdf')
        click_FAQ5_audit = self.find_element(Locators.FAQ5_audit_LOCATOR)

    def FAQ4(self):
        click_FAQ4 = self.find_element(Locators.FAQ4_LOCATOR)
        click_FAQ4.click()
        click_FAQ4_balance_on_compound = self.find_element(Locators.FAQ4_balance_on_compound_LOCATOR).click()
        self.new_window('https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD')
        click_FAQ4_balance_on_eth = self.find_element(Locators.FAQ4_balance_on_eth_LOCATOR).click()
        self.new_window('https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd#tokentxns')
        click_FAQ4_balance_on_compound = self.find_element(Locators.FAQ4_balance_on_bsc_LOCATOR).click()
        self.new_window('https://bscscan.com/address/0xca0648c5b4cea7d185e09fcc932f5b0179c95f17#tokentxns')

    def FAQ3(self):
        click_FAQ3 = self.find_element(Locators.FAQ3_LOCATOR)
        click_FAQ3.click()
        click_FAQ3_article = self.find_element(Locators.FAQ3_article_medium_LOCATOR)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", click_FAQ3_article)
        click_FAQ3_article.click()
        self.new_window('https://defirex.medium.com/how-it-works-6db8679052ad')

    def FAQ2(self):
        click_FAQ2 = self.find_element(Locators.FAQ2_LOCATOR)
        click_FAQ2.click()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        click_FAQ2_article = self.find_element(Locators.FAQ2_article_LOCATOR).click()
        self.new_window('https://www.binance.org/en/blog/defirex-launches-farming-on-ethereum-directly-from-binance-smart-chain/')


    def FAQ1(self):
        click_FAQ1 = self.find_element(Locators.FAQ1_LOCATOR)
        click_FAQ1.click()
        click_FAQ1.click()
        self.driver.execute_script("window.scrollTo(0, 2800)")
        click_FAQ1_git = self.find_element(Locators.FAQ1_git_LOCATOR).click()
        self.new_window('https://github.com/DeFireX')
        click_FAQ1_eth = self.find_element(Locators.FAQ1_owners_eth_LOCATOR).click()
        self.click_top_DAI_funds_holders()
        click_FAQ1_bsc = self.find_element(Locators.FAQ1_owners_bsc_LOCATOR)
        click_FAQ1_bsc.click()
        self.click_top_BSC_BUSD_USDT()
        click_FAQ1_bsc.click()
        self.click_top_DFX_BUSD()
        click_FAQ1_bsc.click()
        self.click_top_DFX()
        click_FAQ1_bsc.click()
        self.click_top_BTCB()
        click_FAQ1_bsc.click()
        self.click_top_BUSD()
        click_FAQ1_bsc.click()
        self.click_top_3POOL_ELIPSIS()
        click_FAQ1_bsc.click()
        self.click_top_BTCB_RENBTC()
        click_FAQ1_bsc.click()
        self.click_top_ETH()
        click_FAQ1_bsc.click()
        self.click_top_XRP()
        click_FAQ1_bsc.click()
        self.click_top_DOT()

    @allure.footer('footer')
    def footer(self):
        click_footer_logo = self.find_element(Locators.footer_logo_LOCATOR).click()
        click_footer_audit = self.find_element(Locators.footer_audit_LOCATOR).click()
        self.new_window(
            'https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf')
        click_footer_contract = self.find_element(Locators.footer_contract_LOCATOR).click()
        self.new_window('https://etherscan.io/address/0xb942ca22e0eb0f2524f53f999ae33fd3b2d58e3e#code')
        click_footer_git = self.find_element(Locators.footer_git_LOCATOR).click()
        self.new_window('https://github.com/DeFireX')
        click_footer_licence = self.find_element(Locators.footer_licence_LOCATOR).click()
        self.new_window('https://www.teatmik.ee/en/captcha')
        click_footer_tg = self.find_element(Locators.footer_tg_LOCATOR).click()
        self.new_window('https://t.me/defirex')
        click_footer_fb = self.find_element(Locators.footer_fb_LOCATOR).click()
        self.new_window('https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2FDeFireX')
        click_footer_medium = self.find_element(Locators.footer_medium_LOCATOR).click()
        self.new_window('https://defirex.medium.com/')
        click_footer_discord = self.find_element(Locators.footer_discord_LOCATOR).click()
        self.new_window('https://discord.com/invite/m6S8pmR')
        click_footer_twitter = self.find_element(Locators.footer_twitter_LOCATOR).click()
        self.new_window('https://twitter.com/DeFireXorg')

    def click_support(self):
        click_support = self.find_element()

    def read_article_and_proofs(self):
        click_read_article = self.find_element(Locators.LOCATOR_read_article).click()
        self.new_window(
            'https://www.binance.org/en/blog/defirex-launches-farming-on-ethereum-directly-from-binance-smart-chain/')
        click_proof_check = self.find_element(Locators.proof_check_locator).click()
        self.new_window(
            'https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd#tokentxns')
        click_read_audit = self.find_element(Locators.read_audit_locator).click()
        self.new_window(
            'https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf')
        click_see_git = self.find_element(Locators.see_git_locator).click()
        self.new_window('https://github.com/DeFireX')
        click_see_guide = self.find_element(Locators.see_guide_locator).click()
        self.new_window('https://defirex.org/assets/data/autonome_client_instruction_en.pdf')

    def menu_clicks(self):
        click_pools = self.find_element(Locators.LOCATOR_pools).click()
        click_wiki = self.find_element(Locators.LOCATOR_wiki).click()
        self.new_window('https://wiki.defirex.org/')
        click_lang = self.find_element(Locators.LOCATOR_lang).click()

    def buy(self):
        click_buy = self.find_element(Locators.LOCATOR_buy_DFX).click()
        self.new_window('https://app.1inch.io/#/56/swap/DFX/BUSD')

    def guarantees(self):
        click_guarantees = self.find_element(Locators.LOCATOR_guarantees).click()
        click_balance_on_etherscan = self.find_element(Locators.LOCATOR_balance_on_etherscan).click()
        self.new_window('https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd')
        click_guarantees = self.find_element(Locators.LOCATOR_guarantees).click()
        click_balance_check_profit = self.find_element(Locators.LOCATOR_check_profit).click()
        self.new_window('https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD')
        click_guarantees = self.find_element(Locators.LOCATOR_guarantees).click()
        click_audit = self.find_element(Locators.LOCATOR_audit).click()
        self.new_window(
            'https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf')
        click_guarantees = self.find_element(Locators.LOCATOR_guarantees).click()
        click_git = self.find_element(Locators.LOCATOR_git).click()
        self.new_window('https://github.com/DeFireX')
        click_guarantees = self.find_element(Locators.LOCATOR_guarantees).click()
        click_how_works = self.find_element(Locators.LOCATOR_how_works).click()
        self.new_window('https://defirex.medium.com/how-it-works-6db8679052ad')

    def holders(self):
        self.click_top_users_balances()
        self.click_top_users_balances_on_Ethereum()
        self.click_top_DAI_funds_holders()
        self.click_top_BSC_holders()
        self.click_top_BSC_BUSD_USDT()
        self.click_top_BSC_holders()
        self.click_top_DFX_BUSD()
        self.click_top_BSC_holders()
        self.click_top_DFX()
        self.click_top_BSC_holders()
        self.click_top_BTCB()
        self.click_top_BSC_holders()
        self.click_top_BUSD()
        self.click_top_BSC_holders()
        self.click_top_3POOL_ELIPSIS()
        self.click_top_BSC_holders()
        self.click_top_BTCB_RENBTC()
        self.click_top_BSC_holders()
        self.click_top_ETH()
        self.click_top_BSC_holders()
        self.click_top_XRP()
        self.click_top_BSC_holders()
        self.click_top_DOT()

    @allure.story('Story1')
    def click_logo(self):
        self.find_element(Locators.LOCATOR_LOGO).click()

    def click_top_users_balances(self):
        click_top_users_balance = self.find_element(Locators.LOCATOR_top_users_balance)
        click_top_users_balance.click()

    @allure.story('Story2')
    def click_top_users_balances_on_Ethereum(self):
        click_top_users_balances_on_Ethereum = self.find_element(Locators.LOCATOR_top_users_balances_on_Ethereum)
        click_top_users_balances_on_Ethereum.click()
        return click_top_users_balances_on_Ethereum

    @allure.story('Story3')
    def click_top_DAI_funds_holders(self):
        click_top_DAI_funds_holders = self.find_element(Locators.LOCATOR_top_DAI_funds_holders)
        click_top_DAI_funds_holders.click()
        self.new_window('https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01')
        return click_top_DAI_funds_holders

    @allure.story('Story4')
    def click_top_BSC_holders(self):
        click_top_users_balance = self.find_element(Locators.LOCATOR_top_users_balance)
        click_top_users_balance.click()
        click_top_BSC_holders = self.find_element(Locators.LOCATOR_top_BSC_holders)
        click_top_BSC_holders.click()
        return click_top_BSC_holders

    @allure.story('Story5')
    def click_top_BSC_BUSD_USDT(self):
        click_top_BSC_BUSD_USDT = self.find_element(Locators.LOCATOR_top_BSC_BUSD_USDT)
        click_top_BSC_BUSD_USDT.click()
        self.new_window('https://www.bscscan.com/token/0x987f04DecE1c5AE9E69cF4F93D00bBE2cA5Af98c')
        return click_top_BSC_BUSD_USDT

    @allure.story('Story6')
    def click_top_DFX_BUSD(self):
        click_top_DFX_BUSD = self.find_element(Locators.LOCATOR_top_DFX_BUSD)
        click_top_DFX_BUSD.click()
        self.new_window('https://www.bscscan.com/token/0xe4743bee99d515a2C36C30B37e3756750fE24c9D')
        return click_top_DFX_BUSD

    @allure.story('Story7')
    def click_top_DFX(self):
        click_top_DFX = self.find_element(Locators.LOCATOR_top_DFX)
        click_top_DFX.click()
        self.new_window('https://www.bscscan.com/token/0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf')
        return click_top_DFX

    @allure.story('Story8')
    def click_top_BTCB(self):
        click_top_BTCB = self.find_element(Locators.LOCATOR_top_BTCB)
        click_top_BTCB.click()
        self.new_window('https://www.bscscan.com/token/0x7CA1fEA7d198cEaE9A319B5EE89E860aAB7D82d7')
        return click_top_BTCB

    @allure.story('Story9')
    def click_top_BUSD(self):
        click_top_BTCB = self.find_element(Locators.LOCATOR_top_BUSD)
        click_top_BTCB.click()
        self.new_window('https://www.bscscan.com/token/0xAB2f29783265940305EA99573AA18bD301911a09')
        return click_top_BTCB

    @allure.story('Story10')
    def click_top_3POOL_ELIPSIS(self):
        click_top_3POOL_ELIPSIS = self.find_element(Locators.LOCATOR_top_3POOL_ELIPSIS)
        click_top_3POOL_ELIPSIS.click()
        self.new_window('https://www.bscscan.com/token/0x5DaA08aF18104702d4a387027E09b9b83b0fc720')
        return click_top_3POOL_ELIPSIS

    @allure.story('Story11')
    def click_top_BTCB_RENBTC(self):
        click_top_BTCB_RENBTC = self.find_element(Locators.LOCATOR_top_BTCB_RENBTC)
        click_top_BTCB_RENBTC.click()
        self.new_window('https://www.bscscan.com/token/0x667D9312535708f105139CF2BBE70bA123573ff2')
        return click_top_BTCB_RENBTC

    @allure.story('Story12')
    def click_top_3POOL_NERVE(self):
        click_top_3POOL_NERVE = self.find_element(Locators.LOCATOR_top_3POOL_NERVE)
        click_top_3POOL_NERVE.click()
        self.new_window('https://www.bscscan.com/token/0x48bFdF75B1315A2D27293fAD7221790f3DfeA1b0')
        return click_top_3POOL_NERVE

    @allure.story('Story13')
    def click_top_ETH(self):
        click_top_ETH = self.find_element(Locators.LOCATOR_top_ETH)
        click_top_ETH.click()
        self.new_window('https://www.bscscan.com/token/0x48bFdF75B1315A2D27293fAD7221790f3DfeA1b0')
        return click_top_ETH

    @allure.story('Story14')
    def click_top_ETH(self):
        click_top_ETH = self.find_element(Locators.LOCATOR_top_ETH)
        click_top_ETH.click()
        self.new_window('https://www.bscscan.com/token/0x735ba150d6A842B1feE3737F023fDdF781CfEaA0')
        return click_top_ETH

    @allure.story('Story15')
    def click_top_XRP(self):
        click_top_XRP = self.find_element(Locators.LOCATOR_top_XRP)
        click_top_XRP.click()
        self.new_window('https://www.bscscan.com/token/0x2df142fc7e0f7164c90c9f93e3012d956c34c299')
        return click_top_XRP

    @allure.story('Story16')
    def click_top_DOT(self):
        click_top_DOT = self.find_element(Locators.LOCATOR_top_DOT)
        click_top_DOT.click()
        self.new_window('https://www.bscscan.com/token/0xaa954f2c619377a61380bfd084359e69d445a856')
        return click_top_DOT

    def click_top_dfx_price(self):
        click_dfx_price = self.find_element(Locators.LOCATOR_DFX_PRICE)
        click_dfx_price.click()
        self.new_window('https://app.1inch.io/#/56/swap/DFX/BUSD')
        return click_dfx_price
