<template>
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
      </l-map>
    </div>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { ref } from 'vue';
import { LMap, LTileLayer } from '@vue-leaflet/vue-leaflet';

const zoom = ref(10);
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
</style>
