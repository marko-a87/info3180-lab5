<template>
    <div class="movies-container">
        <h1 class="page-title">Movies</h1>
        <div class="grid-container">
            <div v-for="movie in movies" :key="movie.id" class="movie-card">
                <div class="card-content">
                    <div class="poster-wrapper">
                        <img :src="`/api/v1/posters/${movie.poster}`" class="poster-img"/>
                    </div>
                    <div class="info">
                        <h2 class="movie-title">{{ movie.title }}</h2>
                        <p class="movie-desc">{{ movie.description }}</p>
                    </div>
                </div>
                
               
            </div>
        </div>
    </div>

</template>

<script setup>
import {ref, onMounted} from "vue";

let movies = ref([]);


const fetchMovies = ()=>{
    fetch("/api/v1/movies",{
    method: "GET",
    })
    .then(response=>response.json())
    .then(data =>{
    // display a success message
    console.log(data);
    movies.value = data.movies
    })
    .catch(function (error) {
    console.log(error);
});

}

onMounted(()=>{
    fetchMovies();
})

</script>

<style>

.movies-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}
.page-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
}


.grid-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
@media (min-width: 640px) {
  .grid-container {
    grid-template-columns: 1fr 1fr;
  }
}
@media (min-width: 1024px) {
  .grid-container {
    grid-template-columns: 1fr 1fr 1fr;
  }
}

/* Card styling */
.movie-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  overflow: hidden;
}


.card-content {
  display: flex;
  min-height: 150px;
}

.poster-wrapper {
  flex: 0 0 100px;
  overflow: hidden;
}
.poster-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}


.info {
  flex: 1;
  padding: 0.75rem 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.movie-title {
  font-size: 1.1rem;
  margin: 0;
  margin-bottom: 0.5rem;
}
.movie-desc {
  margin: 0;
  color: #555;
  line-height: 1.4;
  font-size: 0.95rem;
}

</style>