data {
  int num_teams;
  int num_games;
  vector[num_teams] prior_score;
  int team_1_rank[num_games];
  int team_2_rank[num_games];
  vector[num_games] team_1_score;
  vector[num_games] team_2_score;
  real deg_freedom;
}
transformed data {
  vector[num_games] score_diff;
  vector[num_games] sqrt_diff;
  
  score_diff <- team_1_score - team_2_score;
  
  for (i in 1:num_games)
    // Square-root of score difference
    sqrt_diff[i] <- (step(score_diff[i]) - .5)*sqrt(fabs(score_diff[i]));
}
parameters {
  real b;
  real<lower=0> sigma_a;
  real<lower=0> sigma_y;
  vector[num_teams] a;
}
model {
  a ~ normal(b*prior_score, sigma_a);
  
  for (i in 1:num_games)
    sqrt_diff[i] ~ student_t(deg_freedom, a[team_1_rank[i]] - a[team_2_rank[i]], sigma_y);
}
generated quantities {
  vector[num_games] ypred;
  
  // Compute predictive distribution for each game
  for (i in 1:num_games) {
    ypred[i] = student_t_rng(deg_freedom, a[team_1_rank[i]] - a[team_2_rank[i]], sigma_y);
  }
}
