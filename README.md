# JOJI - AI Customer Care AIaaS

JOJI is a highly capable customer care executive. JOJI is fully capable of understanding any product.

## Portal

The JOJI portal is where you create a project and upload your documents which contains the troubleshooting steps to solve all reported issues.

### Configuration

Help JOJI understand the product by

* reading all the troubleshooting documents/manuals.
* uploading the recordings for customer care resolutions.
* training examples in how JOJI should converse with the customer.
* How JOJI should handle situations where JOJI is not able to resolve the issue.
* Configure how JOJI should behave and act with a number of parameters to play around with
  * Voice
  * Tone
  * Confidence
  * Appearance in Video

### Other

* Record all the conversations JOJI made
* Review and analyze feedback provided for JOJI by customers
* Analyze the data used to train JOJI and how it can be further improved
* Setup roles and responsibilities for your organization and different users
* Managing human customer care executives and rules on when they should be diverted to
* Account managaement, billing, etc.
* Setup languages JOJI should be well versed in.

## Customer Care chat

JOJI can speak to you and solve your issues either through voice/video/chat anytime!

1. The user's speech is converted to text using whisper.
2. The user interacts with JOJI in a conversational manner until JOJI resolves the issue.
3. If JOJI cannot resolve your issue, you can always divert it to a human customer care executive for further clarification.
4. Enable Voice, where text is converted to speech using facebook/fastspeech2
5. Enable Video, where virtual avatar is created for JOJI and the voice would be used to give life to JOJI
6. Standard chatbased resolution
7. Understand images for troubleshooting
8. Can be done over the phone as well

## How to Use

### Poetry

1. Install and create python virtual env
2. Install [poetry](https://python-poetry.org/)
3. Run `poetry install --with dev` to install requirements

### Run Portal

To run the portal simply run

``` bash
streamlit run joji/portal/hello.py
```

### Talk to JOJI

To chat with JOJI

``` basah
streamlit run joji/chat/app.py
```