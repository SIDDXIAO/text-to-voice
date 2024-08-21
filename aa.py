from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import streamlit as st


st.title('Text to speech')

tab1, tab2, = st.tabs(["app","api"])  
with tab2:
    apikey = st.text_input("api-key")
    url = st.text_input("url")
with tab1:
    input_text = st.text_input("Text to convert into speech")
    filename = st.text_input("Enter audio file name with .wav extension")
    voicesel = st.selectbox('voices', ["en-US_AllisonVoice", "en-GB_KateVoice", "en-US_AllisonExpressive", "en-US_EmmaExpressive", "de-DE_DieterVoice", "es-LA_DanielaExpressive", "en-US_LisaExpressive", "en-US_MichaelExpressive", "fr-FR_ReneeVoice", "ko-KR_JinV3Voice", "de-DE_BirgitVoice", "en-AU_HeidiExpressive", "en-AU_JackExpressive", "en-US_MichaelVoice", "pt-BR_IsabelaV3Voice", "it-IT_FrancescaV2Voice", "en-US_LisaV3Voice", "pt-BR_IsabelaVoice", "es-ES_EnriqueVoice", "de-DE_ErikaV3Voice", "es-US_SofiaVoice", "en-GB_JamesV3Voice", "ja-JP_EmiV3Voice", "es-ES_LauraVoice", "en-US_EmilyV3Voice", "fr-FR_ReneeV3Voice", "es-LA_SofiaV3Voice", "es-LA_SofiaVoice", "en-US_AllisonV2Voice", "fr-CA_LouiseV3Voice", "de-DE_BirgitV3Voice", "en-US_LisaV2Voice", "nl-NL_MerelV3Voice", "es-US_SofiaV3Voice", "en-US_KevinV3Voice", "en-US_OliviaV3Voice", "it-IT_FrancescaVoice", "en-GB_CharlotteV3Voice", "en-US_HenryV3Voice", "de-DE_BirgitV2Voice", "en-GB_KateV3Voice", "ja-JP_EmiVoice", "es-ES_LauraV3Voice", "de-DE_DieterV3Voice", "it-IT_FrancescaV3Voice", "es-ES_EnriqueV3Voice", "de-DE_DieterV2Voice", "fr-FR_NicolasV3Voice"])
    if st.button("Generate"):
        authenticator = IAMAuthenticator(apikey)
        text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )

        text_to_speech.set_service_url(url)

        with open(filename, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    input_text,
                    voice=voicesel,
                    accept='audio/wav'        
                ).get_result().content)
        
