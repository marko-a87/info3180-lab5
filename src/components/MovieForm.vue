<template>
    <form @submit.prevent="saveMovie" id="movieForm" method="POST">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control"/>
            <label for="description" class="form-label">Movie description</label>
            <textarea name="description" class="form-control"></textarea>
            <label for="poster" class="form-label">Movie Poster</label>
            <input type="file" name="poster" class="form-control"/>
        </div>
        <button type="submit" name="submit" class="form-control">Submit</button>
    </form>
</template>

<script setup>
import { ref, onMounted } from "vue";
let csrf_token = ref("");
function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
    })
}

onMounted(() => {
    getCsrfToken();
});
const saveMovie = () =>{
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
    'X-CSRFToken': csrf_token.value
    }
    })
    .then(function (response) {
    console.log("Response",response)
    return response.json();
    })
    .then(function (data) {
    // display a success message
    
    console.log(data);
    })
    .catch(function (error) {
    console.log(error);
});
}
</script>


