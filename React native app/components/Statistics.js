import React from "react";
import { StyleSheet, Text, View, Image, ScrollView } from "react-native";
import PChart from "./charts/PChart";
import ProChart from "./charts/ProChart";
import StackedChart from "./charts/StackedChart";
import BaChart from "./charts/BaChart";

export default function Statistics() {
  return (
    <ScrollView>
      <View>
        <Text
          style={{
            paddingLeft: 20,
            paddingTop: 80,
            fontSize: 20,
            paddingBottom: 4,
            textDecorationLine: "underline",
          }}
        >
          Pie Chart :
        </Text>
        <PChart></PChart>
      </View>
      <Text
        style={{
          paddingLeft: 20,
          paddingTop: 20,
          fontSize: 20,
          paddingBottom: 25,
          textDecorationLine: "underline",
        }}
      >
        Progress Chart :
      </Text>
      <ProChart></ProChart>
    </ScrollView>
  );
}
