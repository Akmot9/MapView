<template>
  <div id="map-loading-indicator">
    <p>Applying filters</p>
    <div><n-spin size="small" stroke="#2A96A8" /></div>
  </div>
</template>

<script>
import { NSpin } from 'naive-ui';

export default {
  components: {
    NSpin,
  },
  data() {
    return {};
  },
};
</script>

<style>
#map-loading-indicator {
  height: 90px;
  width: 300px;
  background-color: white;
  position: absolute;
  z-index: 9999;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  border-radius: 6px;
  box-shadow: 2.1px 2.4px 10.4px -23px rgba(0, 0, 0, 0.24),
    5.1px 5.7px 24.9px -23px rgba(0, 0, 0, 0.173),
    9.5px 10.8px 47px -23px rgba(0, 0, 0, 0.143),
    17px 19.2px 83.8px -23px rgba(0, 0, 0, 0.12),
    31.8px 35.9px 156.7px -23px rgba(0, 0, 0, 0.097),
    76px 86px 375px -23px rgba(0, 0, 0, 0.067);
  -moz-box-shadow: 2.1px 2.4px 10.4px -23px rgba(0, 0, 0, 0.24),
    5.1px 5.7px 24.9px -23px rgba(0, 0, 0, 0.173),
    9.5px 10.8px 47px -23px rgba(0, 0, 0, 0.143),
    17px 19.2px 83.8px -23px rgba(0, 0, 0, 0.12),
    31.8px 35.9px 156.7px -23px rgba(0, 0, 0, 0.097),
    76px 86px 375px -23px rgba(0, 0, 0, 0.067);
  -webkit-box-shadow: 2.1px 2.4px 10.4px -23px rgba(0, 0, 0, 0.24),
    5.1px 5.7px 24.9px -23px rgba(0, 0, 0, 0.173),
    9.5px 10.8px 47px -23px rgba(0, 0, 0, 0.143),
    17px 19.2px 83.8px -23px rgba(0, 0, 0, 0.12),
    31.8px 35.9px 156.7px -23px rgba(0, 0, 0, 0.097),
    76px 86px 375px -23px rgba(0, 0, 0, 0.067);
  color: #252526;
}
</style>
