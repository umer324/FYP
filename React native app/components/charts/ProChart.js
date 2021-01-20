import React from "react";
import { StyleSheet, Text, View, Image } from "react-native";
import {
  LineChart,
  BarChart,
  PieChart,
  ProgressChart,
  ContributionGraph,
  StackedBarChart,
} from "react-native-chart-kit";

const data = {
  labels: ["Total", "Accept", "Rejected"],
  data: [1.0, 0.66, 0.33],
};

export default function ProChart() {
  return (
    <ProgressChart
      data={data}
      width={360}
      height={220}
      strokeWidth={16}
      radius={32}
      chartConfig={{
        backgroundColor: "#e26a00",
        backgroundGradientFrom: "#fb8c00",
        backgroundGradientTo: "#ffa726",
        decimalPlaces: 2, // optional, defaults to 2dp
        color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
        labelColor: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
        style: {
          borderRadius: 16,
        },
        propsForDots: {
          r: "6",
          strokeWidth: "2",
          stroke: "#ffa726",
        },
      }}
      paddingLeft="30"
      hideLegend={false}
    />
  );
}
