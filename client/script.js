document.addEventListener('DOMContentLoaded', main);

function main() {
    const button = document.querySelector('button');
    button.addEventListener('click', async () => {
        const input = document.querySelector('input');
        const form = document.querySelector('form');
        for(const item of input.files) {
            const formData = new FormData();
            formData.append('file', item)
            await fetch('http://localhost:8000/uploadfile/',
                {method: 'POST', body: formData})
                .then(data => console.log(data))
                .catch(data => console.log(data))
        }
    })
}
