import streamlit as st
import pandas as pd
import numpy as np
import pickle
from joblib import load
from collections import Counter

# 페이지 설정
st.set_page_config(
    page_title="데이터 기반 신문 구독자 이탈 예측",
    page_icon="🤖",
    layout="wide"
)

# 모델 로드
model = load('best_model.joblib')

# 컬럼 순서
correct_order = [
    "HH Income", "Home Ownership", "dummy for Children", "Year Of Residence",
    "Age", "weekly fee", "Deliveryperiod", "Nielsen Prizm", "reward program",
    "Working", "Gender", "Is_Online"
]


# Encoding Label
languages = {'Amharic': 0, 'Arabic': 1, 'Armenian': 2, 'Chinese': 3, 'Czech': 4, 'Danish': 5, 'Dutch': 6, 'English': 7, 'Farsi (Persian)': 8, 'Finnish': 9, 'French': 10, 'Ga': 11, 'German': 12, 'Greek': 13, 'Hebrew': 14, 'Hindi': 15, 'Hungarian': 16, 'Italian': 17, 'Japanese': 18, 'Khmer (Cambodian)': 19, 'Korean': 20, 'Laotian (Lao)': 21, 'Latvian (Lettish)': 22, 'Norwegian': 23, 'Polish': 24, 'Portuguese': 25, 'Romanian': 26, 'Russian': 27, 'Serbo-Croatian': 28, 'Slovenian': 29, 'Spanish': 30, 'Swedish': 31, 'Tagalog': 32, 'Thai': 33, 'Turkish': 34, 'Urdu': 35, 'Vietnamese': 36}

source_channels = {'AdvAdm': 0, 'Agent': 1, 'Assoc': 2, 'CCAuto': 3, 'CSR': 4, 'Chat': 5, 'CircAdm': 6, 'Contest': 7, 'Counter': 8, 'Crew': 9, 'Crew1': 10, 'Crew2': 11, 'Crew3': 12, 'Crew4': 13, 'CustCall': 14, 'DIRECTM2': 15, 'DIRECTM4': 16, 'DTI': 17, 'DirectMl': 18, 'EMAIL4': 19, 'Email': 20, 'Event': 21, 'Event1': 22, 'FUSS': 23, 'Gift': 24, 'INTERNET': 25, 'InPaper': 26, 'Internet': 27, 'Internt4': 28, 'Kiosk': 29, 'Kiosk1': 30, 'Kiosk2': 31, 'Kiosk3': 32, 'Kiosk4': 33, 'Kiosk5': 34, 'OutMedia': 35, 'PARTNER': 36, 'Partner': 37, 'RetMail': 38, 'RetenIn': 39, 'RetenOut': 40, 'SCINSRT4': 41, 'SCINSRT6': 42, 'SCinsert': 43, 'System': 44, 'TMC': 45, 'TeleIn': 46, 'TeleOut': 47, 'VRU': 48, 'iSrvices': 49}
cities = {'ALISO VIEJO': 0, 'ANAHEIM': 1, 'ARTESIA': 2, 'BREA': 3, 'BUENA PARK': 4, 'CAPISTRANO BEACH': 5, 'CERRITOS': 6, 'CHINO': 7, 'CHINO HILLS': 8, 'CORONA': 9, 'CORONA DEL MAR': 10, 'COSTA MESA': 11, 'CYPRESS': 12, 'DANA POINT': 13, 'DIAMOND BAR': 14, 'FOOTHILL RANCH': 15, 'FOUNTAIN VALLEY': 16, 'FULLERTON': 17, 'GARDEN GROVE': 18, 'HAWAIIAN GARDENS': 19, 'HUNTINGTON BEACH': 20, 'IRVINE': 21, 'LA HABRA': 22, 'LA MIRADA': 23, 'LA PALMA': 24, 'LADERA RANCH': 25, 'LAGUNA BEACH': 26, 'LAGUNA HILLS': 27, 'LAGUNA NIGUEL': 28, 'LAGUNA WOODS': 29, 'LAKE FOREST': 30, 'LAKEWOOD': 31, 'LONG BEACH': 32, 'LOS ALAMITOS': 33, 'MIDWAY CITY': 34, 'MISSION VIEJO': 35, 'MURRIETA': 36, 'NEWPORT BEACH': 37, 'NEWPORT COAST': 38, 'NORCO': 39, 'ORANGE': 40, 'PLACENTIA': 41, 'RANCHO SANTA MARGARITA': 42, 'SAN CLEMENTE': 43, 'SAN JUAN CAPISTRANO': 44, 'SANTA ANA': 45, 'SEAL BEACH': 46, 'SIGNAL HILL': 47, 'SILVERADO': 48, 'STANTON': 49, 'TRABUCO CANYON': 50, 'TUSTIN': 51, 'VILLA PARK': 52, 'WESTMINSTER': 53, 'WHITTIER': 54, 'YORBA LINDA': 55}
counties = {'LOS ANGELES': 0, 'ORANGE': 1, 'RIVERSIDE': 2, 'SAN BERNARDINO': 3}
ethnicities = {'African (other)': 0, 'African American 95%+': 1, 'Albanian': 2, 'Angolan': 3, 'Arab': 4, 'Armenian': 5, 'Austrian': 6, 'Belgian': 7, 'Bhutanese': 8, 'Bulgarian': 9, 'Byelorussian (Belarusian)': 10, 'Chinese': 11, 'Croatian': 12, 'Czech': 13, 'Danish': 14, 'Dutch': 15, 'Egyptian': 16, 'English': 17, 'Estonian': 18, 'Ethiopian': 19, 'Filipino (Philippine)': 20, 'Finnish': 21, 'French': 22, 'German': 23, 'Ghanaian': 24, 'Greek': 25, 'Hawaiian': 26, 'Hispanic': 27, 'Hungarian': 28, 'Indian': 29, 'Indonesian': 30, 'Iraqi': 31, 'Irish': 32, 'Italian': 33, 'Japanese': 34, 'Jewish': 35, 'Kenyan': 36, 'Khmer (Kampuchean, Cambodian)': 37, 'Korean': 38, 'Laotian': 39, 'Latvian': 40, 'Lithuanian': 41, 'Luxembourgian': 42, 'Malawian': 43, 'Myanmar (Burma)': 44, 'Native American (American Indian)': 45, 'Nigerian': 46, 'Norwegian': 47, 'Pakistani': 48, 'Persian': 49, 'Polish': 50, 'Portuguese': 51, 'Romanian': 52, 'Ruandan (Rwandan)': 53, 'Russian': 54, 'Scottish (Scotch)': 55, 'Serbian': 56, 'Slovakian (Slovak)': 57, 'Slovenian (Slovene)': 58, 'Swaziland': 59, 'Swedish': 60, 'Swiss': 61, 'Syrian': 62, 'Thai': 63, 'Turkish': 64, 'Ugandan': 65, 'Ukrainian': 66, 'Vietnamese': 67, 'Welsh': 68, 'Zairian (Democratic Republic of the Con': 69, 'Zimbabwean': 70, 'multi-ethnic': 71, 'unknown': 72}
nielsen_options = {'FE': 0, 'FM': 1, 'FW': 2, 'ME': 3, 'MM': 4, 'MW': 5, 'YE': 6, 'YM': 7, 'YW': 8}
weekly_fees = {'$0': 0, '$0 - $0.01': 1, '$0.01 - $0.50': 2, '$0.51 - $0.99': 3, '$1.00 - $1.99': 4, '$10.00 - $10.99': 5, '$2.00 - $2.99': 6, '$3.00 - $3.99': 7, '$4.00 - $4.99': 8, '$5.00 - $5.99': 9, '$6.00 - $6.99': 10, '$7.00 - $7.99': 11, '$8.00 - $8.99': 12, '$9.00 - $9.99': 13}
delivery_periods = {'7day': 0, '7dayol': 1, '7dayt': 2, 'fri-sun': 3, 'fri-sunt': 4, 'mon-fri': 5, 'omtwtfo': 6, 'satsun': 7, 'soooofs': 8, 'soooofst': 9, 'soooooo': 10, 'soooooot': 11, 'sooooos': 12, 'sooooost': 13, 'soootfs': 14, 'soootfst': 15, 'sun-fri': 16, 'sun-frit': 17, 'sunonly': 18, 'sunonlyt': 19, 'thu-sun': 20, 'thu-sunt': 21}

# ========================
# 탭1: 개별 예측
# ========================

st.markdown("## 👨‍💻 개별 사용자 이탈 예측")

with st.form(key="prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        income = st.text_input("💸HH income 입력(예: 123.45)")
        if income.strip() != "":
            try:
                # 쉼표 입력도 허용하려면 replace(",", "") 추가
                income = float(income.replace(",", "").strip())
            except ValueError:
                st.error("유효한 숫자가 아닙니다. 숫자와 소수점만 입력하세요.")

        age = st.slider("🎂 Age", 18, 90, 30)
        dummy_for_Children_display= st.selectbox('👨🏻‍👩🏻‍👦🏻‍👦🏻아이 여부',['N',"Y"])
        dummy_for_Children = 0 if dummy_for_Children_display == "N" else 1
        weekly_fee_display = st.selectbox("💸 Weekly Fee",['$7.00 - $7.99', '$0.01 - $0.50', '$1.00 - $1.99', '$8.00 - $8.99',
       '$0 - $0.01', '$2.00 - $2.99', '$9.00 - $9.99', '$4.00 - $4.99',
       '$0.51 - $0.99', '$3.00 - $3.99', '$5.00 - $5.99', '$6.00 - $6.99',
       '$10.00 - $10.99', '$0'])
        weekly_fee = weekly_fees[weekly_fee_display]
        
        reward_program = st.slider("🎁 Reward Program", 0, 100, 3)
        delivery_period_display = st.selectbox("🚚 Delivery Period", ['7day', 'sunonly', 'thu-sun', 'satsun', '7dayol', 'sooooos',
       'mon-fri', 'soooofs', 'soooooot', '7dayt', 'fri-sun', 'soootfs',
       'sunonlyt', 'soooooo', 'thu-sunt', 'omtwtfo', 'fri-sunt',
       'soootfst', 'sun-fri', 'sooooost', 'sun-frit', 'soooofst'])
        delivery_period = delivery_periods[delivery_period_display]
        year_of_residence = st.slider("📅 Year Of Residence", 1, 100, 10)
            
    with col2:
        home_ownership_display = st.selectbox("🏠 Home Ownership", ["RENTER", "OWNER"])
        home_ownership = 1 if home_ownership_display == "RENTER" else 0   
        nielsen_options_tr = [
            "MW: Male Working-age (근로 연령대 남성)",
            "MM: Male Middle-aged (중년 남성)",
            "YM: Young Man (젊은 남성)",
            "ME: Male Elderly (노년 남성)",
            "YE: Young Elderly (젊은 노년층)",
            "FM: Female Middle-aged (중년 여성)",
            "FW: Female Working-age (근로 연령대 여성)",
            "YW: Young Woman (젊은 여성)",
            "FE: Female Elderly (노년 여성)",
            "YE: Young Elderly (젊은 노년층)"
        ]

        nielsen_prizm_tr_display = st.selectbox("🧭 Nielsen Prizm", nielsen_options_tr)
        nielsen_prizm_display = {
            "MW: Male Working-age (근로 연령대 남성)" : 'MW',
            "MM: Male Middle-aged (중년 남성)" : 'MM',
            "YM: Young Man (젊은 남성)" : 'YM',
            "ME: Male Elderly (노년 남성)" : 'ME',
            "YE: Young Elderly (젊은 노년층)" : 'YE',
            "FM: Female Middle-aged (중년 여성)" : 'FM',
            "FW: Female Working-age (근로 연령대 여성)" : 'FW',
            "YW: Young Woman (젊은 여성)" : 'YW',
            "FE: Female Elderly (노년 여성)" : 'FE',
            "YE: Young Elderly (젊은 노년층)" : 'YE'}
            
        nielsen_prizm = nielsen_options[nielsen_prizm_display[nielsen_prizm_tr_display]]

        soruce_channel_display = st.selectbox('💻 이용 매체',['CircAdm', 'Partner', 'Internet', 'Crew', 'Kiosk', 'SCinsert',
        'TeleIn', 'CustCall', 'RetenIn', 'DirectMl', 'TeleOut', 'VRU',
        'Kiosk1', 'System', 'Chat', 'AdvAdm', 'TMC', 'Crew1', 'Email',
        'RetenOut', 'InPaper', 'Kiosk4', 'Assoc', 'Event', 'Kiosk2',
        'OutMedia', 'Internt4', 'PARTNER', 'Crew4', 'Kiosk5', 'Counter',
        'Event1', 'FUSS', 'Crew3', 'Crew2', 'INTERNET', 'CSR', 'DIRECTM2',
        'EMAIL4', 'iSrvices', 'DIRECTM4', 'Kiosk3', 'RetMail', 'Gift',
        'SCINSRT4', 'Agent', 'SCINSRT6', 'ExecAdm', 'Contest', 'CCAuto',
        'DTI'])

        soruce_channel = source_channels[soruce_channel_display]
            
        city_display = st.selectbox('🏢도시',['LONG BEACH', 'NEWPORT COAST', 'IRVINE', 'LAGUNA NIGUEL',
        'RANCHO SANTA MARGARITA', 'LADERA RANCH', 'SAN CLEMENTE',
        'BUENA PARK', 'ALISO VIEJO', 'LAGUNA WOODS', 'NEWPORT BEACH',
        'FOOTHILL RANCH', 'TRABUCO CANYON', 'DANA POINT', 'LAGUNA HILLS',
        'LAGUNA BEACH', 'ANAHEIM', 'SANTA ANA', 'FULLERTON', 'LA HABRA',
        'COSTA MESA', 'PLACENTIA', 'HUNTINGTON BEACH', 'CYPRESS',
        'GARDEN GROVE', 'CORONA', 'BREA', 'WESTMINSTER', 'WHITTIER',
        'FOUNTAIN VALLEY', 'VILLA PARK', 'ORANGE', 'TUSTIN', 'STANTON',
        'NORCO', 'DIAMOND BAR', 'LOS ALAMITOS', 'MISSION VIEJO',
        'CERRITOS', 'CORONA DEL MAR', 'SEAL BEACH', 'LAKEWOOD', 'ARTESIA',
        'CHINO', 'LA MIRADA', 'HAWAIIAN GARDENS', 'CHINO HILLS',
        'MIDWAY CITY', 'YORBA LINDA', 'SIGNAL HILL', 'LAKE FOREST',
        'SILVERADO', 'SAN JUAN CAPISTRANO', 'CAPISTRANO BEACH', 'MURRIETA',
        'LA PALMA'])

        city = cities[city_display]

        county_display = st.selectbox('🏦 County',['LOS ANGELES', 'ORANGE', 'RIVERSIDE', 'SAN BERNARDINO'])
        county = counties[county_display]

        language_display = st.selectbox('🗣️언어',['German','English','Italian','Chinese','Spanish','Vietnamese',
        'Farsi (Persian)', 'Japanese', 'Turkish', 'Polish', 'Russian', 'Portuguese',
        'Hebrew', 'Hindi', 'Arabic', 'Korean' ,'Urdu' ,'Czech' ,'Romanian', 'Thai',
        'Khmer (Cambodian)' ,'Danish', 'Amharic' ,'Laotian (Lao)' ,'Swedish',
        'Tagalog','French' ,'Armenian', 'Norwegian' ,'Hungarian' ,'Finnish' ,'Ga',
        'Slovenian' ,'Dutch' ,'Serbo-Croatian' ,'Greek' ,'Latvian (Lettish)'])

        language = languages[language_display]

        ethnicity_display = st.selectbox('🗺인종',['German', 'Italian' ,'English' ,'Scottish (Scotch)', 'Hispanic',
        'Chinese', 'Irish','Swedish' ,'Filipino (Philippine)' ,'Jewish', 'Arab',
        'Japanese' ,'Indian' ,'Vietnamese' ,'Persian' ,'French' ,'Korean' ,'Turkish',
        'Norwegian' ,'Armenian' ,'Polish' ,'Portuguese', 'Dutch' ,'Welsh' ,'Belgian',
        'Byelorussian (Belarusian)' ,'Czech' ,'Thai', 'Ukrainian' ,'African (other)',
        'Danish', 'Native American (American Indian)', 'Zimbabwean', 'Hungarian',
        'Russian' ,'Austrian' ,'Pakistani' ,'Greek' ,'Khmer (Kampuchean, Cambodian)',
        'Lithuanian' ,'Romanian' ,'African American 95%+', 'Egyptian', 'Finnish',
        'Ethiopian' ,'multi-ethnic', 'Slovakian (Slovak)' ,'Serbian' ,'Swiss',
        'Laotian', 'Ugandan' ,'Croatian' ,'Ruandan (Rwandan)', 'Malawian',
        'Indonesian', 'Angolan' ,'Latvian' ,'Iraqi' ,'Hawaiian' ,'Syrian', 'Albanian',
        'Ghanaian', 'Slovenian (Slovene)', 'Kenyan', 'Myanmar (Burma)' ,'Bulgarian',
        'Bhutanese' ,'Swaziland' ,'Nigerian', 'Luxembourgian' ,'Estonian',
        'Zairian (Democratic Republic of the Con'])

        ethnicity = ethnicities[ethnicity_display]

        submitted = st.form_submit_button("예측 실행")

    if submitted:
        input_df = pd.DataFrame([{ 
            "Home Ownership": home_ownership, 'Ethnicity' : ethnicity,
            "dummy for Children": dummy_for_Children, "Year Of Residence": year_of_residence,
            'Language' : language, 'City' : city, 'County' : county, "weekly fee": weekly_fee,
            "Deliveryperiod": delivery_period, 'Nielsen Prizm' : nielsen_prizm, "reward program": reward_program, 
            'reward program' : reward_program, 'Source Channel' : soruce_channel,
            "Age": age, "Income": income, 
        }])

        # row = input_df.iloc[0]  # 첫 행을 Series로
        # st.write(
        #     f"Home Ownership: {row['Home Ownership']}, "
        #     f"Ethnicity: {row['Ethnicity']}, "
        #     f"dummy for Children: {row['dummy for Children']}, "
        #     f"Year Of Residence: {row['Year Of Residence']}, "
        #     f"Language: {row['Language']}, "
        #     f"City: {row['City']}, County: {row['County']}, "
        #     f"weekly fee: {row['weekly fee']}, Deliveryperiod: {row['Deliveryperiod']}, "
        #     f"Nielsen Prizm: {row['Nielsen Prizm']}, reward program: {row['reward program']}, "
        #     f"Source Channel: {row['Source Channel']}, Age: {row['Age']}, Income: {row['Income']}"
        # )
        # st.dataframe(input_df.head())

       

        # input_df = input_df[correct_order]
        # scaled_input = scaler.transform(input_df)
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.markdown("### 📢 예측 결과")
        if prediction[0] == 1:
            st.error("🚨 구독 취소 위험이 **높습니다**.")
        else:
            st.success("✅ 구독 유지 가능성이 **높습니다**.")

        st.markdown(f"**선택 고객의 **구독 취소 위험 확률:** `{prediction_proba[0][1]:.2%}`")



