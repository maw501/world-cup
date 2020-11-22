import numpy as np
import pandas as pd

SPI = "../data/soccerpowerindex.txt"
DP = "../data/worldcup2012.txt"


def load_teams(filepath: str):
    return np.loadtxt(filepath, dtype=str)


def get_teams():
    return load_teams(SPI)


def transformed_prior_scores(
    teams: np.ndarray,
):
    raw_prior_score = np.arange(len(teams), 0, -1)
    prior_score = (raw_prior_score - np.mean(raw_prior_score)) / (
        2 * np.std(raw_prior_score, ddof=1)
    )
    return prior_score


def get_ranking_dict(teams: np.ndarray):
    return {k: v for k, v in zip(teams, range(1, len(teams) + 1))}


def load_score_data(filepath: str):
    data = pd.read_csv(filepath, delim_whitespace=True, header=None)
    data.columns = ["team_1", "team_1_score", "team_2", "team_2_score"]
    return data


def team_1_fave_mask(df: pd.DataFrame):
    return df["team_1_rank"].values < df["team_2_rank"].values


def create_cols(
    df: pd.DataFrame,
    team_1_fave_mask: np.ndarray,
    t1_col: str,
    t2_col: str,
    fave_name: str,
    underdog_name: str,
):
    df[fave_name] = df.loc[team_1_fave_mask, t1_col]
    df.loc[~team_1_fave_mask, fave_name] = df.loc[~team_1_fave_mask, t2_col]
    df[underdog_name] = df.loc[~team_1_fave_mask, t1_col]
    df.loc[team_1_fave_mask, underdog_name] = df.loc[team_1_fave_mask, t2_col]


def get_data():
    teams = get_teams()
    ranking_dict = get_ranking_dict(teams)
    df = load_score_data(DP)

    df["team_1_rank"] = df["team_1"].apply(lambda x: ranking_dict[x])
    df["team_2_rank"] = df["team_2"].apply(lambda x: ranking_dict[x])
    mask = team_1_fave_mask(df)
    create_cols(df, mask, "team_1", "team_2", "fave", "underdog")
    create_cols(
        df,
        mask,
        "team_1_score",
        "team_2_score",
        "fave_score",
        "underdog_score",
    )
    create_cols(
        df,
        mask,
        "team_1_rank",
        "team_2_rank",
        "fave_rank",
        "underdog_rank",
    )

    df["abs_rank_diff"] = np.abs(
        df["team_1_rank"].values - df["team_2_rank"].values
    )
    df["fave_underdog_score_diff"] = (
        df["fave_score"].values - df["underdog_score"].values
    )
    df = df.sort_values(["abs_rank_diff", "fave"], ascending=[False, True])
    return df


def get_prior_scores():
    teams = get_teams()
    return transformed_prior_scores(teams)
