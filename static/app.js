const submitForm = document.querySelector('#submit-form');
const shareForm = document.querySelector('#share-form');
const pfbOutput = document.querySelector('#pfb_output');
const shareOutput = document.querySelector('#share_output');

submitForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(submitForm);
    const response = await fetch('/submit_pfb', {
        method: 'POST',
        body: formData
    });

    const responseJson = await response.json();
    pfbOutput.innerText = responseJson.response_text;
});

shareForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const height = document.querySelector('#height').value;
    const namespaceId = document.querySelector('#namespace_id').value;

    const url = `/namespaced_shares/${namespaceId}/height/${height}`;
    const response = await fetch(url, {
        method: 'POST'
    });

    const responseJson = await response.json();
    shareOutput.innerText = responseJson.response_text;
});
