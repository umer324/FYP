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

const pieData = [
  {
    name: "Total Inspect",
    population: 20,
    color: "rgba(0, 167, 234, 1)",
    legendFontColor: "#7F7F7F",
    legendFontSize: 14,
  },
  {
    name: "Accepted",
    population: 15,
    color: "green",
    legendFontColor: "#7F7F7F",
    legendFontSize: 15,
  },
  {
    name: "Rejected",
    population: 5,
    color: "red",
    legendFontColor: "#7F7F7F",
    legendFontSize: 15,
  },
];

export default function PChart() {
  return (
    <PieChart
      data={pieData}
      width={320}
      height={200}
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
      paddingLeft="10"
      paddingRight="200"
      accessor="population"
      backgroundColor="transparent"
      absolute
    />
  );
}
