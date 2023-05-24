<template>
  <div
    id="map-filter"
    :class="{
      expanded: filterIsVisible,
      condensed: !filterIsVisible,
      disabled: !isFilterInteractive,
    }"
  >
    <div class="basic-hover-style" @click="toggleFilterVisibility">
      <div v-if="this.filterIsVisible" class="headline">Map filters</div>
      <div class="filter-visibility-toggler">
        <span
          v-if="!filterIsVisible"
          style="vertical-align: top; margin-right: 8px; color: black"
          >(<b>{{ selectedFilters.length }}</b
          >)</span
        >
        <n-icon size="20"
          ><Eye20Filled v-if="this.filterIsVisible" /><EyeOff16Filled v-else
        /></n-icon>
      </div>
    </div>
    <span v-if="this.filterIsVisible">
      <div class="section">
        SOURCES
        <span
          class="clear-all-text interactive-element"
          v-if="this.checkedTypes.length > 0"
          @click="isFilterInteractive ? (this.checkedTypes = []) : ''"
          >Clear all</span
        >
      </div>
      <div style="padding: 10px">
        <div
          v-for="option in this.sourceTypes"
          :key="option"
          :class="[
            'single-option interactive-element',
            this.checkedTypes.includes(option) ? 'checked' : '',
          ]"
        >
          <input
            type="checkbox"
            :id="option"
            :value="option"
            v-model="this.checkedTypes"
            class="interactive-element"
            :disabled="isFilterInteractive ? false : true"
          />
          <label :for="option" class="interactive-element">{{ option }}</label>
        </div>
      </div>
      <div class="section">
        DATE<span
          class="clear-all-text interactive-element"
          v-if="this.dateRange?.length > 0"
          @click="isFilterInteractive ? (this.dateRange = null) : ''"
          >Clear all</span
        >
      </div>
      <div style="padding: 10px">
        <n-date-picker
          class="interactive-element"
          v-model:value="dateRange"
          type="daterange"
          :shortcuts="rangeShortcuts"
          :first-day-of-week="0"
          :format="dateFormat"
          :value-format="dateFormat"
          end-placeholder="To"
          start-placeholder="From"
          :disabled="isFilterInteractive ? false : true"
        >
        </n-date-picker>
      </div>
    </span>
  </div>
</template>

<script>
import { NIcon, NDatePicker } from 'naive-ui';
import { EyeOff16Filled, Eye20Filled } from '@vicons/fluent';

//We import map filter options instead of hardcoding them, because it's likely
//we will be generating the options dynamically based on the available data
import { sourceTypes } from './mapFilterOptions';

function createDebounce() {
  let timeout = null;
  return function (fnc, delayMs) {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      fnc();
    }, delayMs || 2500);
  };
}

export default {
  name: 'MapFilter',
  components: { NIcon, EyeOff16Filled, Eye20Filled, NDatePicker },
  props: ['options', 'isDataBeingLoaded'],
  data() {
    return {
      isFilterVisible: true,
      sourceTypes: sourceTypes,
      dateTypes: ['From', 'To'],
      checkedTypes: [],
      debounce: createDebounce(),
      dateRange: null,
      rangeShortcuts: {
        Today: () => {
          const cur = new Date().getTime();
          return [cur, cur];
        },
        '2 days ago': () => {
          const cur = new Date().getTime();
          var currentDate = new Date();
          currentDate.setDate(currentDate.getDate() - 2);
          return [currentDate.getTime(), cur];
        },
        'Week ago': () => {
          const cur = new Date().getTime();
          var currentDate = new Date();
          currentDate.setDate(currentDate.getDate() - 7);
          return [currentDate.getTime(), cur];
        },
        '2 weeks ago': () => {
          const cur = new Date().getTime();
          var currentDate = new Date();
          currentDate.setDate(currentDate.getDate() - 14);
          return [currentDate.getTime(), cur];
        },
        'Month ago': () => {
          const cur = new Date().getTime();
          var currentDate = new Date();
          currentDate.setDate(currentDate.getDate() - 30);
          return [currentDate.getTime(), cur];
        },
      },
      dateFormat: 'dd/MM/yyyy',
    };
  },
  computed: {
    filterIsVisible() {
      return this.isFilterVisible;
    },
    isFilterInteractive() {
      return !this.isDataBeingLoaded;
    },
    selectedFilters() {
      return this.dateRange
        ? [...this.checkedTypes, ...this.dateRange]
        : this.checkedTypes;
      // return [...this.checkedTypes, ...this.dateRange];
    },
  },
  watch: {
    selectedFilters() {
      this.debounce(() => this.$emit('change-filters', this.selectedFilters));
    },
  },
  methods: {
    toggleFilterVisibility() {
      this.isFilterVisible = !this.isFilterVisible;
    },
  },
};
</script>

<style scoped>
#map-filter {
  background-color: #f2f2f2;
  margin: 10px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0px 1.8px 5.3px rgba(0, 0, 0, 0.069),
    0px 6px 17.9px rgba(0, 0, 0, 0.101), 0px 27px 80px rgba(0, 0, 0, 0.17);
  -moz-box-shadow: 0px 1.8px 5.3px rgba(0, 0, 0, 0.069),
    0px 6px 17.9px rgba(0, 0, 0, 0.101), 0px 27px 80px rgba(0, 0, 0, 0.17);
  -webkit-box-shadow: 0px 1.8px 5.3px rgba(0, 0, 0, 0.069),
    0px 6px 17.9px rgba(0, 0, 0, 0.101), 0px 27px 80px rgba(0, 0, 0, 0.17);
  transition: width 0.4s ease-in-out, height 0.4s ease-in-out;
  -webkit-transition: width 0.4s ease-in-out, height 0.4s ease-in-out;
  -moz-transition: width 0.4s ease-in-out, height 0.4s ease-in-out;
  -o-transition: width 0.4s ease-in-out, height 0.4s ease-in-out;
}

#map-filter.disabled .interactive-element {
  opacity: 0.5;
  cursor: no-drop;
}
#map-filter.expanded {
  width: 300px;
  height: 480px;
}
#map-filter.condensed {
  width: 70px;
  height: 50px;
}
.headline {
  color: #979394;
  font-weight: 400;
  text-align: left;
  padding: 15px 10px 10px 10px;
}
.section {
  color: #252526;
  font-weight: 700;
  background-color: #eaeaed;
  padding: 10px;
}
.filter-visibility-toggler {
  position: absolute;
  top: 25px;
  right: 25px;
  color: #575456;
}
.single-option {
  padding: 5px;
  margin-top: 5px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  width: 100%;
  -webkit-transition: background-color 0.3s ease-in-out;
  -moz-transition: background-color 0.3s ease-in-out;
  -o-transition: background-color 0.3s ease-in-out;
  -ms-transition: background-color 0.3s ease-in-out;
  transition: background-color 0.3s ease-in-out;
}
.single-option.checked {
  background-color: #66c1bf;
  color: white;
}
.single-option input {
  accent-color: white;
  margin: 0px 0px 0px 5px;
}
.single-option label {
  flex-grow: 1;
  padding-left: 10px;
}
.single-option:hover,
.single-option label:hover,
.single-option input:hover {
  cursor: pointer;
  opacity: 0.9;
}
.clear-all-text {
  color: #35b6b4;
  float: right;
}
.clear-all-text:hover {
  cursor: pointer;
  opacity: 0.9;
}

/* Override datepicker styles */
.n-date-panel {
  display: flex !important;
}
.n-date-panel-actions {
  align-items: inherit !important;
}
.n-date-panel-actions__prefix {
  max-width: 150px !important;
  display: block !important;
}
.n-date-panel-actions__prefix .n-button {
  width: 100% !important;
}
.n-date-panel-actions__suffix {
  position: absolute !important;
  right: 10px !important;
}
</style>
