<template>
  <div style="width: 300px">
    <div style="font-weight: 700; margin-bottom: 15px">
      SIGN IN LOGS ({{ logs.length }})
    </div>
    <div>
      <n-table>
        <thead style="display: table; width: 100%">
          <tr>
            <th>Address</th>
            <th>Name</th>
            <th style="text-align: right">Threat</th>
          </tr>
        </thead>
        <n-scrollbar style="max-height: 300px">
          <tbody style="display: table; width: 100%; word-break: break-all">
            <tr v-for="(log, index) in logs" :key="index">
              <td>{{ log.address }}</td>
              <td>{{ log.name }}</td>
              <td>
                <n-popover
                  v-if="log.abuse !== 'None' || log.threatintelname !== 'None'"
                  trigger="hover"
                  placement="top"
                  raw
                >
                  <template #trigger
                    ><NIcon size="15"> <ExclamationTriangle /> </NIcon>
                  </template>
                  <div style="background-color: #fff; padding: 5px 10px">
                    <p>
                      <b>Abuse:</b> {{ log.abuse === 'None' ? '-' : log.abuse }}
                    </p>
                    <p>
                      <b>Intel name:</b>
                      {{
                        log.threatintelname === 'None'
                          ? '-'
                          : log.threatintelname
                      }}
                    </p>
                  </div>
                </n-popover>
                <div v-else></div>
              </td>
            </tr>
          </tbody>
        </n-scrollbar>
      </n-table>
    </div>
  </div>
</template>

<script>
import { NScrollbar, NTable, NPopover, NIcon } from 'naive-ui';
import { ExclamationTriangle } from '@vicons/fa';


export default {
  name: 'MapPopover',
  components: { NScrollbar, NTable, NPopover, NIcon, ExclamationTriangle },
  props: ['logs'],
  data() {
    return {};
  },
};
</script>

<style></style>
