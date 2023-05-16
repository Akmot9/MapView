<template>
  <div v-for="message in messages" :key="message.abuse" class="messages">
      <p>Abuse: {{ message.abuse }}</p>
      <p>Address: {{ message.address }}</p>
      <p>Lat: {{ message.lat }}</p>
      <p>Lng: {{ message.lng }}</p>
      <p>Name: {{ message.name }}</p>
      <p>Threat Intel Name: {{ message.threatintelname }}</p>
      <hr>
        

  </div>
  <div id="container">
    <div id="mapContainer">
      <l-map
        v-model="zoom"
        v-model:zoom="zoom"
        :center="[43.12442, 5.92836]"
        :options="{ attributionControl: false }"
        class="disabled-map"
      >
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          layer-type="base"
          name="OpenStreetMap"
          :max-zoom="12"
        />
        <l-marker v-for="message in messages" :key="message.abuse" 
          :lat-lng="[message.lat, message.lng]"
        > </l-marker>
      
      </l-map>
    </div>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css"
import { ref ,onMounted} from 'vue'
import { 
  LMap, 
  LTileLayer,
  LMarker 
} from '@vue-leaflet/vue-leaflet'

const zoom = ref(10)

const messages = ref([])

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/signin-logs");
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }
    const data = await response.json();
    messages.value = data;
  } catch (error) {
    console.error(error);
  }
});
</script>

<style scoped>
#container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#mapContainer {
  width: 600px;
  height: 400px;
  border: 1px solid #ccc;
}

.messages {
  color: black;
}
</style>
